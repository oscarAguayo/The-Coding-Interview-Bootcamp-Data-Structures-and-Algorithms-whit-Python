import types
from reverse_int import reverse_int

def test_reverse_int_function_exist():
    assert isinstance(reverse_int, types.FunctionType)

def test_zero():
    assert reverse_int(0) == 0

def test_reverse_positive_number():
    assert reverse_int(15) == 51
    assert reverse_int(981) == 189
    assert reverse_int(500) == 5
    assert reverse_int(5) == 5
    assert reverse_int(90) == 9
    assert reverse_int(2359) == 9532


def test_reverse_negative_number():
    assert reverse_int(-15) == -51
    assert reverse_int(-90) == -9
    assert reverse_int(-5) == -5
    assert reverse_int(-2359) == -9532
