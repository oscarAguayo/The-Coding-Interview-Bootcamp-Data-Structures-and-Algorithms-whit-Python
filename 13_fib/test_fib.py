import types
from fib import fib

def test_fib_function_exist():
    assert isinstance(fib, types.FunctionType)

def test_fib_value_for_1():
    assert fib(1) == 1

def test_fib_value_for_2():
    assert fib(2) == 1

def test_fib_value_for_3():
    assert fib(3) == 2

def test_fib_value_for_4():
    assert fib(4) == 3

def test_fib_value_for_39():
    assert fib(39) == 63245986