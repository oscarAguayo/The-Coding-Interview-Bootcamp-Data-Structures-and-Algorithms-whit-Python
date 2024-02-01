import main

def test_zero():
    assert main.reverse_int(0) == 0

def test_reverse_positive_number():
    assert main.reverse_int(15) == 51
    assert main.reverse_int(981) == 189
    assert main.reverse_int(500) == 5
    assert main.reverse_int(5) == 5
    assert main.reverse_int(90) == 9
    assert main.reverse_int(2359) == 9532


def test_reverse_negative_number():
    assert main.reverse_int(-15) == -51
    assert main.reverse_int(-90) == -9
    assert main.reverse_int(-5) == -5
    assert main.reverse_int(-2359) == -9532
