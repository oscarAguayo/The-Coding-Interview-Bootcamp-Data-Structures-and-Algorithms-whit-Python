import main

def test_reverse_int():
    assert main.reverse_int(15) == 51
    assert main.reverse_int(981) == 189
    assert main.reverse_int(500) == 5
    assert main.reverse_int(-15) == -51
    assert main.reverse_int(-90) == -9