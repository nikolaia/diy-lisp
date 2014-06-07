# -*- coding: utf-8 -*-

from .types import Environment, LispError, Closure
from .ast import is_boolean, is_atom, is_symbol, is_list, is_closure, is_integer
from .asserts import assert_exp_length, assert_valid_definition, assert_boolean
from .parser import unparse

"""
This is the Evaluator module. The `evaluate` function below is the heart
of your language, and the focus for most of parts 2 through 6.

A score of useful functions is provided for you, as per the above imports, 
making your work a bit easier. (We're supposed to get through this thing 
in a day, after all.)
"""


def evaluate(ast, env):
	
	if (not isinstance(ast, list)): return ast
	
	if (ast[0] == "quote"): return ast[1]
	elif (ast[0] == "atom"): return is_atom(ast,env)
	elif (ast[0] == "eq"): return is_equal(ast,env)

	elif (ast[0] == "+"): return do_addition(ast, env)
	elif (ast[0] == "-"): return do_subtraction(ast, env)
	elif (ast[0] == "/"): return do_division(ast, env)
	elif (ast[0] == "*"): return do_multiplication(ast, env)
	elif (ast[0] == "mod"): return do_mod(ast, env)
	elif (ast[0] == ">"): return do_greater(ast, env)

def is_atom(ast, env):
	if (isinstance(ast[1], list) and ast[1][0] == "quote"): 
		return evaluate(["atom", ast[1][1]],env)
	return evaluate(ast[1], env) == ast[1]

def is_equal(ast, env):
	if (evaluate(["atom", ast[1]], env) and evaluate(["atom", ast[2]], env)):
		return ast[1] == ast[2]
	else: return False

def is_number(number, env):
	if (evaluate(number, env) == number and number is not True and number is not False):
		return True
	else: raise LispError("Not a number")

def do_addition(ast, env):
	if (is_number(ast[1], env) and is_number(ast[2], env)):
		return ast[1] + ast[2]

def do_subtraction(ast, env):
	if (is_number(ast[1], env) and is_number(ast[2], env)):
		return ast[1] - ast[2]

def do_division(ast, env):
	if (is_number(ast[1], env) and is_number(ast[2], env)):
		return ast[1] / ast[2]

def do_multiplication(ast, env):
	if (is_number(ast[1], env) and is_number(ast[2], env)):
		return ast[1] * ast[2]

def do_mod(ast, env):
	if (is_number(ast[1], env) and is_number(ast[2], env)):
		return ast[1] % ast[2]

def do_greater(ast, env):
	if (is_number(ast[1], env) and is_number(ast[2], env)):
		return ast[1] > ast[2]
