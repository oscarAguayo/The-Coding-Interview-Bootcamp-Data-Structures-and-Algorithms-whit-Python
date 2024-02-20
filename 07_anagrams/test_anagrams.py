import types
from anagrams import anagrams

def test_anagrams_function_exist():
    assert isinstance(anagrams, types.FunctionType)

def test_hello_is_anagram_of_llohe():
    assert anagrams("hello", "llohe") == True

def test_whoa_hi_anagram():
    assert anagrams("Whoa! Hi!", "Hi! Whoa!") == True

def test_one_one_not_anagram():
    assert anagrams("One One", "Two two two") == False

def test_one_one_not_anagram_2():
    assert anagrams("One one", "One one c") == False

def test_a_tree_life_a_bench_is_not_anagram():
    assert anagrams("A tree, a life, a bench", "A tree, a fence, a yard") == False