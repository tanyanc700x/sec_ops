# outside_input = int(input("Dare to add 4 random digits: "))
# for x in str(outside_input):
#     print(x)


outside_input = int(input("Dare to add 4 random digits: "))

# Получаем каждую цифру числа и выводим её
while outside_input > 0:
    digit = outside_input % 10
    print(digit)
    outside_input //= 10
