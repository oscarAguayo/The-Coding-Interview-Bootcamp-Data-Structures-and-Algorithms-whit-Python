import types
from pyramid import pyramid

def test_pyramid_function_exist():
    assert isinstance(pyramid, types.FunctionType)

def test_pyramid_of_2(capsys):
    pyramid(2)
    captured = capsys.readouterr()
    all_outputs = captured.out.splitlines()
    assert all_outputs[0] == ' # '
    assert all_outputs[1] == '###'
    assert len(all_outputs) == 2

def test_pyramid_of_3(capsys):
    pyramid(3)
    captured = capsys.readouterr()
    all_outputs = captured.out.splitlines()
    assert all_outputs[0] == '  #  '
    assert all_outputs[1] == ' ### '
    assert all_outputs[2] == '#####'
    assert len(all_outputs) == 3

def test_pyramid_of_4(capsys):
    pyramid(4)
    captured = capsys.readouterr()
    all_outputs = captured.out.splitlines()
    assert all_outputs[0] == '   #   '
    assert all_outputs[1] == '  ###  '
    assert all_outputs[2] == ' ##### '
    assert all_outputs[3] == '#######'
    assert len(all_outputs) == 4