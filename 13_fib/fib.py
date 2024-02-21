# --- Directions
# Print out the n-th entry in the fibonacci series.
# The fibonacci series is an ordering of numbers where
# each number is the sum of the preceeding two.
# For example, the sequence
#  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# forms the first ten entries of the fibonacci series.
# Example:
#   fib(4) === 3

def fib(n: int) -> int:
    pass

if __name__ == "__main__":
    n = int(input("Give a number: "))
    r = fib(n)
    print(f"The {n} th fib position is {r}")