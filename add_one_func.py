def add_one(some_list):
    number = 0

    for digit in some_list:
        number = number * 10 + digit

    updated_list = []  # Move this line up to initialize the list
    number += 1

    while number > 0:
        digit = number % 10
        updated_list.insert(0, digit)
        number //= 10
    return updated_list  # Correct the return statement



# Test cases
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
