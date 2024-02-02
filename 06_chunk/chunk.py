# --- Directions
# Given a list and chunk size, divide the list into many sublist
# where each sublist is of length size
# --- Examples
# chunk([1, 2, 3, 4], 2) --> [[ 1, 2], [3, 4]]
# chunk([1, 2, 3, 4, 5], 2) --> [[ 1, 2], [3, 4], [5]]
# chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) --> [[ 1, 2, 3], [4, 5, 6], [7, 8]]
# chunk([1, 2, 3, 4, 5], 4) --> [[ 1, 2, 3, 4], [5]]
# chunk([1, 2, 3, 4, 5], 10) --> [[ 1, 2, 3, 4, 5]]

def chunk(data: list, size: int) -> list:
    final_list = []
    tmp_list = []
    for i, value in enumerate(data, start=1):
        tmp_list.append(value)
        if i % size == 0 or i == len(data):
            final_list.append(tmp_list.copy())
            tmp_list.clear()
    return final_list

if __name__ == "__main__":
    data = eval(input("Give a list: "))
    size = int(input("Give a chunk size: "))
    print(chunk(data, size))