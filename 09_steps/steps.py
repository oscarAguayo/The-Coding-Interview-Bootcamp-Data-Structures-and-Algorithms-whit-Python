# --- Directions
# Write a function that accepts a positive number N.
# The function should console log a step shape
# with N levels using the # character.  Make sure the
# step has spaces on the right hand side!
# --- Examples
#   steps(2)
#       '# '
#       '##'
#   steps(3)
#       '#  '
#       '## '
#       '###'
#   steps(4)
#       '#   '
#       '##  '
#       '### '
#       '####'

def steps(n: int) -> None:
    for i in range(1, n+1):
        print(i*'#'+(n-i)*' ')

if __name__ == "__main__":
    steps(int(input("Give a positive number: ")))