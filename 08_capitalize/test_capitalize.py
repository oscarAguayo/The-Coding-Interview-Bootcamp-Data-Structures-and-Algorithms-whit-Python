import types
from capitalize import capitalize

def test_capitalize_function_exist():
    assert isinstance(capitalize, types.FunctionType)

def test_capitalize_text_one():
    assert capitalize("hi there, how is it going?") == "Hi There, How Is It Going?"

def test_capitalize_text_two():
    assert capitalize("i love breakfast at bill miller bbq") == "I Love Breakfast At Bill Miller Bbq"