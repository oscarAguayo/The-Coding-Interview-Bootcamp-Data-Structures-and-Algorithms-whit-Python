import types
from steps import steps

def test_steps_function_exist():
    assert isinstance(steps, types.FunctionType)

def test_steps_with_1(capsys):
    steps(1)
    captured = capsys.readouterr()
    all_outputs = captured.out.splitlines()
    assert all_outputs[0] == "#"
    assert len(all_outputs) == 1

def test_steps_with_2(capsys):
    steps(2)
    captured = capsys.readouterr()
    all_outputs = captured.out.splitlines()
    assert all_outputs[0] == "# "
    assert all_outputs[1] == "##"
    assert len(all_outputs) == 2

def test_steps_with_3(capsys):
    steps(3)
    captured = capsys.readouterr()
    all_outputs = captured.out.splitlines()
    assert all_outputs[0] == "#  "
    assert all_outputs[1] == "## "
    assert all_outputs[2] == "###"
    assert len(all_outputs) == 3