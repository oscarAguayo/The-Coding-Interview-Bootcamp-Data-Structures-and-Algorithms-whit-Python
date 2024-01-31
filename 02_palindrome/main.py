import re

def palindrome(text: str) -> bool:
# --- Directions
# Given a string, return true if the string is a palindrome
# or false if it is not.  Palindromes are strings that
# form the same word if it is reversed. *Do* include spaces
# and punctuation in determining if the string is a palindrome.
# --- Examples:
#   palindrome("Anita lava la tina") == True
#   palindrome("Amó la paloma") == True
#   palindrome("¡Ojo! corre poco perro cojo") == True
#   palindrome("Allí ni cocina, ni cocinilla") == True
    text = text.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
    pattern = '[^a-zA-Z]'
    normalize_text = re.sub(pattern, '', text).lower()
    return normalize_text == ''.join(list(normalize_text)[::-1])

if __name__ == "__main__":
    print(f"Is palindrome?: {palindrome(input('Given a palindrome: '))}")