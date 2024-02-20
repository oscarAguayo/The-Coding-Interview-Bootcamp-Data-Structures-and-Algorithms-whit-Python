import types
from chunk import chunk

def test_chunk_function_exist():
    assert isinstance(chunk, types.FunctionType)

def test_chunk():
    assert chunk([1, 2, 3, 4], 2) == [[ 1, 2], [3, 4]]
    assert chunk([1, 2, 3, 4, 5], 2) == [[ 1, 2], [3, 4], [5]]
    assert chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) == [[ 1, 2, 3], [4, 5, 6], [7, 8]]
    assert chunk([1, 2, 3, 4, 5], 4) == [[ 1, 2, 3, 4], [5]]
    assert chunk([1, 2, 3, 4, 5], 10) == [[ 1, 2, 3, 4, 5]]

def test_chunk_10_elements_in_size_2():
    assert chunk([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2) == [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]

def test_chunk_3_elements_in_size_1():
    assert chunk([1, 2, 3], 1) == [[1], [2], [3]]

def test_chunk_5_elements_in_size_3():
    assert chunk([1, 2, 3, 4, 5], 3) == [[1, 2, 3], [4, 5]]

def test_chunk_13_elements_in_size_5():
    assert chunk([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 5) == [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13]]