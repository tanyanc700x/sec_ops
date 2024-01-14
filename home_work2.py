
# A request to add digits
outside_input = int(input("Dare to add 4 random digits: "))

# Printing the results using the modulo operator % and the floor division operator // to extract digits
print(outside_input // 1000)
print((outside_input % 1000) // 100)
print((outside_input % 100) // 10)
print(outside_input % 10)


print('Home work done, at a girl!')
