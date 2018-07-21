from lmfit import Parameters
import numpy as np
import pytest

from lmfit_varpro import SeparableModel
from .test_helpers import assert_epsilon


class OneCompartmentDecay(SeparableModel):

    def data(self, **kwargs):
        data = [kwargs['data'][0, :]]
        return data

    def c_matrix(self, parameter, *args, **kwargs):
        parameter = parameter.valuesdict()
        kinpar = np.array([parameter["p0"]])
        c = np.exp(np.outer(np.array(kwargs['times']), -kinpar))
        return [c]

    def e_matrix(self, parameter, **kwargs):
        return np.array([[1.0]])

    def get_test_param_dict(self):
        rparams = [101e-4]
        params = [100e-5]
        wanted_e_matrix = [1.0]
        result_is_e_matrix = True
        test_param_dict = {"rparams": rparams,
                           "params": params,
                           "wanted_params": rparams,
                           "wanted_e_matrix": wanted_e_matrix,
                           "result_is_e_matrix": result_is_e_matrix}
        return test_param_dict


class TwoComparmentDecay(SeparableModel):

    def data(self, **kwargs):
        data = [kwargs['data'][0, :]]
        return data

    def c_matrix(self, parameter, *args, **kwargs):
        kinpar = np.array([parameter["p0"], parameter["p1"]])
        c = np.exp(np.outer(kwargs['times'], -kinpar))
        return [c]

    def e_matrix(self, parameter, **kwargs):
        return np.array([[1.0, 2.0]])

    def get_test_param_dict(self):
        rparams = [101e-4, 202e-5]
        params = [100e-5, 200e-6]
        wanted_e_matrix = [1.0, 2.0]
        result_is_e_matrix = True
        test_param_dict = {"rparams": rparams,
                           "params": params,
                           "wanted_params": rparams,
                           "wanted_e_matrix": wanted_e_matrix,
                           "result_is_e_matrix": result_is_e_matrix}
        return test_param_dict


class MultiChannelMultiCompartmentDecay(SeparableModel):

    wavenum = np.arange(12820, 15120, 4.6)

    def data(self, **kwargs):
        data = [kwargs['data'][i, :] for i in
                range(self.wavenum.shape[0])]
        return data

    def c_matrix(self, parameter, *args, **kwargs):
        kinpar = np.array([parameter["p{}".format(i)] for i in
                           range(len((parameter)))])
        c = np.exp(np.outer(kwargs['times'], -kinpar))
        return [c for _ in range(self.wavenum.shape[0])]

    def e_matrix(self, parameter, **kwargs):
        location = np.array(
            [14705, 13513, 14492, 14388, 14184, 13986])
        delta = np.array([400, 1000, 300, 200, 350, 330])
        amp = np.array([1, 0.1, 10, 100, 1000, 10000])

        E = np.empty((self.wavenum.shape[0], location.shape[0]),
                     dtype=np.float64,
                     order="F")

        for i in range(location.size):
            E[:, i] = amp[i] * np.exp(
                -np.log(2) * np.square(
                    2 * (self.wavenum - location[i])/delta[i]
                )
            )
        return E

    def get_test_param_dict(self):
        rparams = [.006667, .006667, 0.00333, 0.00035, 0.0303, 0.000909]
        params = [.005, 0.003, 0.00022, 0.0300, 0.000888]
        wanted_params = [.006667, 0.00333, 0.00035, 0.0303, 0.000909]
        result_is_e_matrix = False
        test_param_dict = {"rparams": rparams,
                           "params": params,
                           "wanted_params": wanted_params,
                           "result_is_e_matrix": result_is_e_matrix}
        return test_param_dict


@pytest.mark.parametrize("compartment_decay_model",
                         [
                             TwoComparmentDecay,
                             OneCompartmentDecay,
                             MultiChannelMultiCompartmentDecay
                          ])
def test_compartment_decay(compartment_decay_model):

    model = compartment_decay_model()
    times = np.arange(0, 1500, 1.5)

    test_param_dict = model.get_test_param_dict()

    rparams = test_param_dict["rparams"]

    real_params = Parameters()
    for index, rparam in enumerate(rparams):
        real_params.add("p{}".format(index), rparam)

    data = model.eval(real_params, times=times)

    params = test_param_dict["params"]

    initial_parameter = Parameters()
    for index, param in enumerate(params):
        initial_parameter.add("p{}".format(index), param)

    result = model.fit(initial_parameter, False, [], times=times, data=data)

    wanted_params = test_param_dict["wanted_params"]

    for index, wanted_param in enumerate(wanted_params):
        fit_value = result.fitresult.params["p{}".format(index)].value
        assert_epsilon(wanted_param, fit_value)

    if test_param_dict["result_is_e_matrix"]:
        wanted_e_matrix = test_param_dict["wanted_e_matrix"]
        amplitudes = result.e_matrix(data, times=times, data=data)[0]
        for amplitude, want in zip(amplitudes, wanted_e_matrix):
            assert_epsilon(amplitude, want)
    else:
        fitted = result.eval(times=times, data=data)
        assert_epsilon(data, fitted)
