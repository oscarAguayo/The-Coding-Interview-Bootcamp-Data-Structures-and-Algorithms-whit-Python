import types
from matrix import matrix

def test_matrix_function_exist():
    assert isinstance(matrix, types.FunctionType)

def test_matrix_2x2():
    m = matrix(2)
    assert len(m) == 2
    assert m[0] == [1, 2]
    assert m[1] == [4, 3]

def test_matrix_3x3():
    m = matrix(3)
    assert len(m) == 3
    assert m[0] == [1, 2, 3]
    assert m[1] == [8, 9, 4]
    assert m[2] == [7, 6, 5]

def test_matrix_4x4():
    m = matrix(4)
    assert len(m) == 4
    assert m[0] == [1, 2, 3, 4]
    assert m[1] == [12, 13, 14, 5]
    assert m[2] == [11, 16, 15, 6]
    assert m[3] == [10, 9, 8, 7]