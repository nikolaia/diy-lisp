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
	
	if is_atom(ast): 
		if is_symbol(ast):
			return env.lookup(ast)
		return ast

	if (ast[0] == "define"): return eval_define(ast, env)
	if (ast[0] == "if"): return eval_if(ast, env)

	if (ast[0] == "quote"): return ast[1]
	elif (ast[0] == "atom"): return eval_atom(ast,env)
	elif (ast[0] == "eq"): return eval_equal(ast,env)

	elif (ast[0] == "+"): return do_addition(ast, env)
	elif (ast[0] == "-"): return do_subtraction(ast, env)
	elif (ast[0] == "/"): return do_division(ast, env)
	elif (ast[0] == "*"): return do_multiplication(ast, env)
	elif (ast[0] == "mod"): return do_mod(ast, env)
	elif (ast[0] == ">"): return do_greater(ast, env)

def eval_define(ast, env):
	if (len(ast) is not 3): 
		raise LispError("Wrong number of arguments")
	key = ast[1]
	if not is_symbol(key):
		raise LispError("First argument is a non-symbol")
	value = evaluate(ast[2], env)
	env.set(key, value)

def eval_if(ast, env):
	arg1 = evaluate(ast[1], env)
	if (arg1):
		return evaluate(ast[2], env)
	else: return evaluate(ast[3], env)

def eval_atom(ast, env):
	arg = evaluate(ast[1],env)
	return not isinstance(arg, list)

def eval_equal(ast, env):
	if (evaluate(["atom", ast[1]], env) and evaluate(["atom", ast[2]], env)):
		return evaluate(ast[1], env) == evaluate(ast[2], env)
	else: 
		return False

def is_number(number):
	if (isinstance(number, int)):
		return True
	else: raise LispError("Not a number")

def do_addition(ast, env):
	arg1 = evaluate(ast[1], env)
	arg2 = evaluate(ast[2], env)
	if (is_number(arg1) and is_number(arg2)):
		return arg1 + arg2

def do_subtraction(ast, env):
	arg1 = evaluate(ast[1], env)
	arg2 = evaluate(ast[2], env)
	if (is_number(arg1) and is_number(arg2)):
		return arg1 - arg2

def do_division(ast, env):
	arg1 = evaluate(ast[1], env)
	arg2 = evaluate(ast[2], env)
	if (is_number(arg1) and is_number(arg2)):
		return arg1 / arg2

def do_multiplication(ast, env):
	arg1 = evaluate(ast[1], env)
	arg2 = evaluate(ast[2], env)
	if (is_number(arg1) and is_number(arg2)):
		return arg1 * arg2

def do_mod(ast, env):
	arg1 = evaluate(ast[1], env)
	arg2 = evaluate(ast[2], env)
	if (is_number(arg1) and is_number(arg2)):
		return arg1 % arg2

def do_greater(ast, env):
	arg1 = evaluate(ast[1], env)
	arg2 = evaluate(ast[2], env)
	if (is_number(arg1) and is_number(arg2)):
		return arg1 > arg2
