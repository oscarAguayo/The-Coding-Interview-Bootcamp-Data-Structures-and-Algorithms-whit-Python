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
    val = 0
    fib_list = []
    for i in range(n+1):
        if i == 0 or i == 1:
            fib_list.append(i)
            val = i
        else:
            val = fib_list[i-2] + fib_list[i-1]
            fib_list.append(val)
    return val

if __name__ == "__main__":
    n = int(input("Give a number: "))
    r = fib(n)
    print(f"The {n} th fib position is {r}")