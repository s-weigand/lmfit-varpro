from lmfit import Minimizer
from lmfit.minimizer import MinimizerResult
from scipy.optimize import nnls
import numpy as np

from .util import dot
from .qr_decomposition import qr_residual


class SeparableModelResult(Minimizer):

    def __init__(self,
                 model,
                 initial_parameter,
                 nnls,
                 equality_constraints,
                 *args, **kwargs):
        self._model = model
        self.nnls = nnls
        self.equality_constraints = equality_constraints
        self._result = None
        super(SeparableModelResult, self).__init__(self._residual,
                                                   initial_parameter,
                                                   fcn_args=args,
                                                   fcn_kws=kwargs,
                                                   )

    def get_model(self):
        return self._model

    def fit(self, *args, **kwargs):
        verbose = kwargs['verbose'] if 'verbose' in kwargs else 2
        self._result = self.minimize(method='least_squares',
                                     ftol=kwargs.get('ftol', 1e-10),
                                     gtol=kwargs.get('gtol', 1e-10),
                                     verbose=verbose)

    def e_matrix(self, *args, **kwargs):
        return self._model.retrieve_e_matrix(self._result.params,
                                             *args, **kwargs)

    def c_matrix(self, *args, **kwargs):
        return self._model.c_matrix(self._result.params, *args, **kwargs)

    def eval(self, *args, **kwargs):
        e = self.e_matrix(*args, **kwargs)
        c = self.c_matrix(*args, **kwargs)
        return dot(e, c)

    @property
    def fitresult(self) -> MinimizerResult:
        """The lmfit.MinimizerResult returned by the minimization."""
        return self._result

    def final_residual(self, *args, **kwargs):
        return np.asarray([r for r in
                           self._all_residuals(self._result.params, *args,
                                               **kwargs)])

    def final_residual_svd(self, *args, **kwargs):
        residual = self.final_residual(*args, **kwargs)
        lsvd, svals, rsvd = np.linalg.svd(residual)
        return lsvd, svals, rsvd

    # @profile
    def _residual(self, parameter, *args, **kwargs):

        if self.nnls:
            residuals = np.concatenate(list(self._all_residuals_nnls(parameter,
                                                                     *args,
                                                                     **kwargs))
                                       )
        else:
            residuals = np.concatenate(list(self._all_residuals(parameter,
                                                                *args,
                                                                **kwargs)))
        return residuals

    def _all_residuals(self, parameter, *args, **kwargs):

        data_group = self._model.data(**kwargs)
        c_matrix_group = self._model.c_matrix(parameter,
                                              *args, **kwargs)
        for data, c_mat in iter(data_group, c_matrix_group):
            res = self._calculate_residual_qr(data, c_mat)
            yield(res)
        if len(self.equality_constraints) is not 0:
            for constraint in self.equality_constraints:
                emin = constraint.erange[0]
                emax = constraint.crange[1]
                cmin = constraint.crange[0]
                cmax = constraint.erange[1]
                c = [c[cmin:cmax, :] for c in c_matrix_group if emin <=
                     c_matrix_group.index(c) <= emax]
                e_matrix = self._model.retrieve_e_matrix_for_c(c, data)
                yield constraint.calculate(e_matrix, parameter)

    def _calculate_residual_qr(self, data, c_matrix):
        return qr_residual(c_matrix, data)

    def _all_residuals_nnls(self, parameter, *args, **kwargs):

        data_group = self._model.data(**kwargs)
        c_matrix_group = self._model.c_matrix(parameter,
                                              *args, **kwargs)
        e_matrix = []

        for data, c_mat in iter(data_group, c_matrix_group):
            e = self._calculate_e_nnls(data, c_mat)

            yield np.dot(c_mat, e) - data
            e_matrix.append(e)

        if len(self.equality_constraints) is not 0:
            for constraint in self.equality_constraints:
                emin = constraint.erange[0]
                emax = constraint.crange[1]
                yield constraint.calculate(e_matrix[emin: emax])

    def _calculate_e_nnls(self, data, c_matrix):
        result, _ = nnls(c_matrix, data)
        return result


def iter(data, c_matrix):
    for i in range(len(data)):
        yield data[i], c_matrix[i]
