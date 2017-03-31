import warnings
import numpy as np
from .result import SeparableModelResult
from .qr_decomposition import qr_coefficents


class SeparableModel(object):

    def c_matrix(self, parameter, *args, **kwargs):
        raise NotImplementedError

    def e_matrix(self, **kwarg):
        raise NotImplementedError("'self.e_matrix' not defined in model.")

    def data(self, **kwargs):
        raise NotImplementedError

    def eval(self, parameter, *args, **kwargs):
        e = self.e_matrix(parameter, **kwargs)
        c = self.c_matrix(parameter, *args, **kwargs)
        noise = kwargs["noise"] if "noise" in kwargs else False
        res = np.empty((len(c), len(e)), dtype=np.float64)

        for x, t in iter_c_and_e(c, e):
            res[x, t] = np.dot(c[x][t, :], e[t][x, :].T)

        if noise:
            if "noise_seed" in kwargs:
                noise_seed = kwargs["noise_seed"]
                if not isinstance(noise_seed, int):
                    warnings.warn("Warning noise_seed should be integer, seed"
                                  " value of {} reduced to {}"
                                  .format(noise_seed, int(noise_seed)))
                    noise_seed = int(noise_seed)
                np.random.seed(noise_seed)
            std_dev = kwargs["noise_std_dev"] if "noise_std_dev" in kwargs \
                else 1.0
            res = np.random.normal(res, std_dev)
        return res

    def fit(self, initial_parameter, *args, **kwargs):
        result = SeparableModelResult(self, initial_parameter, *args,
                                      **kwargs)
        result.fit(initial_parameter, *args, **kwargs)
        return result

    def retrieve_e_matrix(self, parameter, *args, **kwargs):
        data = self.data(**kwargs)[0]
        c_matrix = self.c_matrix(parameter, *args, **kwargs)
        e_matrix = np.empty((c_matrix.shape[2], data.shape[1]),
                            dtype=np.float64)

        for i in range(data.shape[1]):
            b = data[:, i]
            qr = qr_coefficents(c_matrix[i, :, :], b)
            e_matrix[:, i] = qr[:c_matrix.shape[2]]
        return e_matrix


def iter_c_and_e(c, e):
    for i in range(len(c)):
        for j in range(len(e)):
            yield i, j
