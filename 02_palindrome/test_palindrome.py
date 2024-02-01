from palindrome import palindrome

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