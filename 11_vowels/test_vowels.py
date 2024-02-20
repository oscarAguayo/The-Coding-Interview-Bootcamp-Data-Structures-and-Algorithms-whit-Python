import types
from vowels import vowels

def test_vowels_function_exist():
    assert isinstance(vowels, types.FunctionType)

def test_vowels_in_lowercase():
    assert vowels("aeiou") == 5

def test_vowels_in_uppercase():
    assert vowels("AEIOU") == 5

def test_vowels_in_abecedary():
    assert vowels("abcdefghijklmnopqrstuvwxyz") == 5

def test_not_vowels():
    assert vowels("bcdfghjkl") == 0