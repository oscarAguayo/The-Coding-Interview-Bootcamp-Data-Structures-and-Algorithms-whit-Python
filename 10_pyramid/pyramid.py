# --- Directions
# Write a function that accepts a positive number N.
# The function should console log a pyramid shape
# with N levels using the # character.  Make sure the
# pyramid has spaces on both the left *and* right hand sides
# --- Examples
#   pyramid(1)
#       '#'
#   pyramid(2)
#       ' # '
#       '###'
#   pyramid(3)
#       '  #  '
#       ' ### '
#       '#####'

def pyramid(n: int) -> None:
    for i in range(1, n+1):
        spaces = " "*(n - i)
        symbols = "#"*((i*2) - 1)
        print(spaces+symbols+spaces)

if __name__ == "__main__":
    pyramid(int(input("Give a positive number: ")))