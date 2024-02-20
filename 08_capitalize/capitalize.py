# --- Directions
# Write a function that accepts a string.  The function should
# capitalize the first letter of each word in the string then
# return the capitalized string.
# --- Examples
#   capitalize('a short sentence') --> 'A Short Sentence'
#   capitalize('a lazy fox') --> 'A Lazy Fox'
#   capitalize('look, it is working!') --> 'Look, It Is Working!'

def capitalize(text: str) -> str:
    # return text.title()
    return " ".join([''.join([char.upper() if i == 0 else char for i, char in enumerate(part)]) for part in text.split()])

if __name__ == "__main__":
    print(capitalize(input("Give a string: ")))