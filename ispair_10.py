def is_even(digit):

    return digit % 2 == 0

assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')


######################################
# def is_even(digit):
#     result = digit % 2 == 0
#     print(f"Результат для числа {digit}: {result}")
#     return result
#
# assert is_even(2) == True, 'Test1'
# assert is_even(5) == False, 'Test2'
# assert is_even(0) == True, 'Test3'
# print('OK')
