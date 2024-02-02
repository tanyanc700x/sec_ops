def add_one(some_list):
    number = 0

    for digit in some_list:
        number = number * 10 + digit

    number += 1
    updated_list = str(number)
    return updated_list

# Test cases
assert add_one([1, 2, 3, 4]) == '1235', 'Test1'
assert add_one([9, 9, 9]) == '1000', 'Test2'
assert add_one([0]) == '1', 'Test3'
assert add_one([9]) == '10', 'Test4'
print("OK")
