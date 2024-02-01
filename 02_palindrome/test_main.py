import main

def test_palindrome():
    assert main.palindrome("abba") == True
    assert main.palindrome("abcdefg") == False
    assert main.palindrome("aba") == True
    assert main.palindrome(" aba") == False
    assert main.palindrome("aba ") == False
    assert main.palindrome("greetings") == False
    assert main.palindrome("1000000001") == True
    assert main.palindrome("Fish hsif") == False
    assert main.palindrome("pennep") == True