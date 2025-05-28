import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])
def test_bubble_sort_too_many():
    expected_result = 1 
    test_arr = [64, 34, 25, 12, 22, 11, 90, 100, 200, 300, 400]
    test_result = Lab3.bubble_sort(test_arr, 1)
    assert (test_result == expected_result)

def test_bubble_sort_empty():
    expected_result = 0
    test_arr = []
    test_result = Lab3.bubble_sort(test_arr,1)
    assert (test_result == expected_result)

def test_bubble_non_integer():
    test_arr = [34.43,4,3,4,2]
    expected_result =  2
    test_result = Lab3.bubble_sort(test_arr,1)
    assert (test_result == expected_result)