import types
from palindrome import palindrome

def test_palindrome_function_exist():
    assert isinstance(palindrome, types.FunctionType)

def test_palindrome():
    assert palindrome("abba") == True
    assert palindrome("abcdefg") == False
    assert palindrome("aba") == True
    assert palindrome(" aba") == False
    assert palindrome("aba ") == False
    assert palindrome("greetings") == False
    assert palindrome("1000000001") == True
    assert palindrome("Fish hsif") == False
    assert palindrome("pennep") == True