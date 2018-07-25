# -*- coding: utf-8 -*-

"""Top-level package for lmfit-varpro."""

__author__ = """Joris Snellenburg, Stefan Schuetz, Joern Weissenborn"""
__email__ = 'j.snellenburg@gmail.com, YamiNoKeshin@gmail.com, joern.weissenborn@gmail.com'
__version__ = '0.0.2'

from . import constraints, separable_model, result

SeparableModel = separable_model.SeparableModel

SeparableModelResult = result.SeparableModelResult


CompartmentEqualityConstraint = constraints.CompartmentEqualityConstraint
