
# A request to add digits
outside_input = int(input("Dare to add 4 random digits: "))

# Printing the results using the modulo operator % and the floor division operator // to extract digits
print(outside_input // 1000)
print((outside_input % 1000) // 100)
print((outside_input % 100) // 10)
print(outside_input % 10)
# #
# #
# # Using divmod method.
# # # A request to add digits
# # outside_input = int(input("Dare to add 4 random digits: "))
# #
# # # Extraction process
# # thousands, left = divmod(outside_input, 1000)
# # hundreds,left = divmod(left, 100)
# # tens,ones = divmod(left, 10)
# #
# # # Results printing
# # print(thousands)
# # print(hundreds)
# # print(tens)
# # print(ones)

