from max_char import max_char

def test_max_char():
    assert max_char("abcccccccd") == "c"
    assert max_char("abcdefghijklmnaaaaa") == "a"

def test_max_char_with_numbers():
    assert max_char("apple 1231111") == "1"
    assert max_char("ab1c1d1e1f1g1") == "1"