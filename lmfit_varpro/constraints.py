import numpy as np


class CompartmentEqualityConstraint(object):
    """
    An CompartmentEqualityConstraint adds a penalty to the residual if 2
    compartments of the e matrix differ more than by just a scaling parameter
    in the sum over a given range. It calculates as

        penalty = weight * (parameter * sum(c[range, i]) - c[range, j])
    """
    def __init__(self, weight, i, j, parameter, range):
        self.weight = weight
        """Weight factor of the penalty"""

        self.i = i
        """Index of the first compartment"""

        self.j = j
        """Index of the second compartment"""

        self.parameter = parameter
        """Index of the parameter"""

        self.range = range
        """The range the constraint is applied on"""

    def calculate(self, e_matrix, parameter):
        p = parameter[self.parameter].value
        range = e_matrix[self.range[0]:self.range[1], :]
        return self.weight * (p * np.sum(range[self.i] - range[self.j]))
