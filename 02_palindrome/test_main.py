import main

def test_palindrome():
    assert main.palindrome("abba") == True
    assert main.palindrome("abcdefg") == False
    assert main.palindrome("Anita lava la tina") == True