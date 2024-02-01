## --- Directions
## Given a string, return the character that is most
## commonly used in the string.
## --- Examples
## max_char("abcccccccd") == "c"
## max_char("apple 1231111") == "1"

def max_char(text: str) -> dict:
    data = {text.count(char): char for char in set(text)}
    return data.get(max(data))

if __name__ == "__main__":
    print(f"The most character commonly used in string is: {max_char(input('Give a string: '))}")