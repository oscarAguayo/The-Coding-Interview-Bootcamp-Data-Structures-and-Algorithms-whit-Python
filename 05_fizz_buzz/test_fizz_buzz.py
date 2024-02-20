import types
from fizz_buzz import fizz_buzz

def test_fizz_buzz_function_exist():
    assert isinstance(fizz_buzz, types.FunctionType)

def test_length_of_5_elements(capsys):
    fizz_buzz(5)
    captured = capsys.readouterr()
    all_outputs = captured.out.splitlines()
    assert len(all_outputs) == 5

def test_fizz_buzz_values_of_15(capsys):
    fizz_buzz(15)
    captured = capsys.readouterr()
    all_outputs = captured.out.splitlines()
    assert all_outputs[0] == "1"
    assert all_outputs[1] == "2"
    assert all_outputs[2] == "fizz"
    assert all_outputs[3] == "4"
    assert all_outputs[4] == "buzz"
    assert all_outputs[5] == "fizz"
    assert all_outputs[6] == "7"
    assert all_outputs[7] == "8"
    assert all_outputs[8] == "fizz"
    assert all_outputs[9] == "buzz"
    assert all_outputs[10] == "11"
    assert all_outputs[11] == "fizz"
    assert all_outputs[12] == "13"
    assert all_outputs[13] == "14"
    assert all_outputs[14] == "fizzbuzz"
    assert len(all_outputs) == 15