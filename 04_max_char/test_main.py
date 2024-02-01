import main

def test_max_char():
    assert main.max_char("abcccccccd") == "c"
    assert main.max_char("abcdefghijklmnaaaaa") == "a"

def test_max_char_with_numbers():
    assert main.max_char("apple 1231111") == "1"
    assert main.max_char("ab1c1d1e1f1g1") == "1"