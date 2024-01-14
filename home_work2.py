
# A request to add digits
outside_input = int(input("Dare to add 4 random digits: "))

# Printing the results using the modulo operator % and the floor division operator // to extract digits
print(outside_input // 1000)
print((outside_input % 1000) // 100)
print((outside_input % 100) // 10)
print(outside_input % 10)
# #
#
# A request to add digits
outside_input = int(input("Dare to add 4 random digits: "))

# Extraction process
thousands, left1 = divmod(outside_input, 1000)
hundreds, left2 = divmod(left1, 100)
tens, ones = divmod(left2, 10)

# Results printing
print(thousands)
print(hundreds)
print(tens)
print(ones)

# outside_input = int(input("Dare to add 4 random digits: "))
# for x in str(outside_input):
#     print(x)


# outside_input = int(input("Dare to add 4 random digits: "))
#
# # Getting a number
# while outside_input > 0:
#     digit = outside_input % 10
#     print(digit)
#     outside_input //= 10

