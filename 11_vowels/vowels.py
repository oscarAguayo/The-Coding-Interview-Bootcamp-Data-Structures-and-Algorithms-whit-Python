# --- Directions
# Write a function that returns the number of vowels
# used in a string.  Vowels are the characters 'a', 'e'
# 'i', 'o', and 'u'.
# --- Examples
#   vowels('Hi There!') --> 3
#   vowels('Why do you ask?') --> 4
#   vowels('Why?') --> 0
import re

def vowels(text: str) -> int:
    return len(re.findall(r"[aeiouAEIOU]", text))

if __name__ == "__main__":
    print(vowels(input("Give a text: ")))