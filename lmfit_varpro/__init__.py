# -*- coding: utf-8 -*-

"""Top-level package for lmfit-varpro."""

__author__ = """Joris Snellenburg, Stefan Schuetz, Joern Weissenborn"""
__email__ = 'j.snellenburg@gmail.com, YamiNoKeshin@gmail.com, joern.weissenborn@gmail.com'

from . import constraints, separable_model, result

SeparableModel = separable_model.SeparableModel

SeparableModelResult = result.SeparableModelResult


CompartmentEqualityConstraint = constraints.CompartmentEqualityConstraint

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
