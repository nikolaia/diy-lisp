# -*- coding: utf-8 -*-

"""
This module holds some types we'll have use for along the way.

It's your job to implement the Closure and Environment types.
The LispError class you can have for free :)
"""


class LispError(Exception):
    """General lisp error class."""
    pass


class Closure:
    def __init__(self, env, params, body):
        raise NotImplementedError("DIY")

    def __str__(self):
        return "<closure/%d>" % len(self.params)


class Environment:
    def __init__(self, variables=None):
        self.variables = variables if variables else {}

    def lookup(self, symbol):
        try:
            return self.variables[symbol]
        except KeyError:
            raise LispError("%s has not been defined", symbol)

    def extend(self, variables):
        new_variables = self.variables.copy()
        new_variables.update(variables)
        return Environment(new_variables)

    def set(self, symbol, value):
        if symbol in self.variables:
            raise LispError("Symbol already defined.")
        self.variables[symbol] = value