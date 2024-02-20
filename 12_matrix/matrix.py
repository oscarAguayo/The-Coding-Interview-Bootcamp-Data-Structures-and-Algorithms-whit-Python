# --- Directions
# Write a function that accepts an integer N
# and returns a NxN spiral matrix.
# --- Examples
#   matrix(2)
#     [[1, 2],
#     [4, 3]]
#   matrix(3)
#     [[1, 2, 3],
#     [8, 9, 4],
#     [7, 6, 5]]
#  matrix(4)
#     [[1,   2,  3, 4],
#     [12, 13, 14, 5],
#     [11, 16, 15, 6],
#     [10,  9,  8, 7]]

def matrix(n_matrix: int) -> list:
    t_matrix = [[0 for _ in range(n_matrix)] for __ in range(n_matrix)]
    numbers = [_ for _ in range(1, n_matrix*n_matrix+1)]
    x = 0
    max_x = n_matrix -1
    min_x = 0
    y = 0
    max_y = n_matrix -1
    min_y = 0
    loops = 0
    for n in numbers:
        # left upper corner
        if  x == min_x and x < max_x and y == min_y and y < max_y:
            if n_matrix -1 != max_y:
                loops += 1
            if loops != 0:
                max_x -= 1
            t_matrix[x][y] = n
            y += 1
        # move to the right
        elif x == min_x and y < max_y:
            t_matrix[x][y] = n
            y += 1
        # right upper corner
        elif  x == min_x and y == max_y:
            if loops != 0:
                min_y += 1
            t_matrix[x][y] = n
            x += 1
        # move down
        elif x < max_x and y == max_y:
            t_matrix[x][y] = n
            x += 1
        # right lower corner
        elif x == max_x and y == max_y:
            min_x += 1
            t_matrix[x][y] = n
            y -= 1
        # move to the left
        elif x == max_x and y > min_y:
            t_matrix[x][y] = n
            y -= 1
        # left lower corner
        elif x == max_x and y == min_y:
            max_y -= 1
            t_matrix[x][y] = n
            x -= 1
        # move up
        elif x > min_x and y == min_y:
            t_matrix[x][y] = n
            x -= 1
    return t_matrix

if __name__ == "__main__":
    for raw in matrix(int(input("Give an integer: "))):
        print(raw)