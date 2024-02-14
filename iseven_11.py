def is_even(number):
    return str(number)[-1] in {'0', '2', '4', '6', '8'}

# Тести
assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('OK')
#
#
# #########################################################
# def is_even(number):
#     return (number & 1) == 0
#     #  return bool(number & 1) == False
#
# assert is_even(2494563894038**2) == True, 'Test1'
# assert is_even(1056897**2) == False, 'Test2'
# assert is_even(24945638940387**3) == False, 'Test3'
# print('OK')

############################################################


