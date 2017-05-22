import numpy as np


class CompartmentEqualityConstraint(object):
    """
    An CompartmentEqualityConstraint adds a penalty to the residual if 2
    compartments of the e matrix differ more than by just a scaling parameter
    in the sum over a given range. It calculates as

        penalty = weight * (parameter * sum(c[range, i]) - c[range, j])
    """
    def __init__(self, weight, i, j, parameter, erange, crange):
        self.weight = weight
        """Weight factor of the penalty"""

        self.i = i
        """Index of the first compartment"""

        self.j = j
        """Index of the second compartment"""

        self.parameter = parameter
        """Index of the parameter"""

        self.erange = erange
        """The range on the e matrix axis the constraint is applied on"""

        self.crange = crange
        """The range on the c matrix axis the constraint is applied on"""

    def calculate(self, e_matrix, parameter):
        p = parameter[self.parameter].value
        return self.weight * (p * np.sum(e_matrix[self.i] - e_matrix[self.j]))
