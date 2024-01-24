my_list = [0, 1, 7, 2, 4, 8]
# my_list = [1, 3, 5]
# my_list = [6]
# my_list = [0]
# my_list = []
result = my_list[0::2]
if len(my_list) >= 1:
    math = sum(x for x in result) * my_list[-1]
else:
    math = 0
print("Final amount is", math)


