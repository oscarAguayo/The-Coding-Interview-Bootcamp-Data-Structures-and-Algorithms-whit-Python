from fizz_buzz import fizz_buzz

def test_length_of_5_elements():
    data = fizz_buzz(5)
    assert len(data) == 5

def test_fizz_buzz_values_of_15():
    data = fizz_buzz(15)
    assert data[0] == 1
    assert data[1] == 2
    assert data[2] == "fizz"
    assert data[3] == 4
    assert data[4] == "buzz"
    assert data[5] == "fizz"
    assert data[6] == 7
    assert data[7] == 8
    assert data[8] == "fizz"
    assert data[9] == "buzz"
    assert data[10] == 11
    assert data[11] == "fizz"
    assert data[12] == 13
    assert data[13] == 14
    assert data[14] == "fizzbuzz"
    for i in data:
        print(i)