def reverse_int(n: int) -> int:
# --- Directions
# Given an integer, return an integer that is the reverse
# ordering of numbers.
# --- Examples
#   reverse_int(15) == 51
#   reverse_int(981) == 189
#   reverse_int(500) == 5
#   reverse_int(-15) == -51
#   reverse_int(-90) == -9
    aux_int = int(''.join(list(str(n).replace('-', ''))[::-1]))
    return aux_int * -1 if n < 0 else aux_int

if __name__ == "__main__":
    print(f"Reverse is: {reverse_int(int(input('Given a integer: ')))}")