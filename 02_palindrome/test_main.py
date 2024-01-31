import main

def test_palindrome():
    assert main.palindrome("Anita lava la tina") == True
    assert main.palindrome("Amó la paloma") == True
    assert main.palindrome("¡Ojo! corre poco perro cojo") == True
    assert main.palindrome("Allí ni cocina, ni cocinilla") == True