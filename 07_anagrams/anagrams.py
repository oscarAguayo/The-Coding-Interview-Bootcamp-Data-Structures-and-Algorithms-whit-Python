## --- Directions
## Check to see if two provided strings are anagrams of eachother.
## One string is an anagram of another if it uses the same characters
## in the same quantity. Only consider characters, not spaces
## or punctuation.  Consider capital letters to be the same as lower case
## --- Examples
##   anagrams('rail safety', 'fairy tales') --> True
##   anagrams('RAIL! SAFETY!', 'fairy tales') --> True
##   anagrams('Hi there', 'Bye there') --> False

import re

def anagrams(stringA: str, stringB: str) -> bool:
    normalize_a = re.sub(r"\W", '', stringA).lower()
    normalize_b = re.sub(r"\W", '', stringB).lower()
    return sorted(list(normalize_a)) == sorted(list(normalize_b))

if __name__ == "__main__":
    stringA = input("Give a string A: ")
    stringB = input("Give a string B: ")
    print(f"Are the strings anagrams?: {anagrams(stringA, stringB)}")