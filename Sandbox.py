# ######################################### Tuples #######################################################################x
# thistuple = ("apple", "banana", "cherry")
# print(thistuple)
#
# thistuple = ("apple",)
# print(type(thistuple))
#
# #NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))
#
# list = [1,2,3,4,4,4,5]
# testtuple = tuple(list)
# print(type(testtuple))
# print(testtuple)
#
#
# a = 2
# b = 330
# print("A") if a > b else print("B")
# a = 200
# b = 33
# c = 500
# if a > b and c > a:
#   print("Both conditions are True")
#
#   i = 1
#   while i < 6:
#       print(i)
#       i += 1
#
#
# def case_one():
#     print("One")
#
# def case_two_or_three():
#     print("Two or Three")
#
# def default_case():
#     print("Default case")
#
# switch_dict = {
#     1: case_one,
#     2: case_two_or_three,
#     3: case_two_or_three
# }
#
# x = 2
# switch_dict.get(x, default_case)()
#




#
# import sys
#
# testtuple = ("apple", "banana", "cherry")
#
# initial_memory_size = sys.getsizeof(testtuple)
# print(f"Initial size of tuple: {initial_memory_size} bytes")
#
# for i in range(9):
#     testtuple += ("new_item",)
#     updated_memory_size = sys.getsizeof(testtuple)
#     print(f"Iteration {i + 1}: Updated size of tuple: {updated_memory_size} bytes")
#
# final_memory_size = sys.getsizeof(testtuple)
# print(f"Final size of tuple: {final_memory_size} bytes")


# import sys
#
# testlist = ["apple", "banana", "cherry"]
#
#
# initial_memory_size = sys.getsizeof(testlist)
# print(f"Initial size of list: {initial_memory_size} bytes")
#
# for i in range(9):
#     testlist += ["new_item"]
#     updated_memory_size = sys.getsizeof(testlist)
#     print(f"Iteration {i + 1}: Updated size of list: {updated_memory_size} bytes")
#
# final_memory_size = sys.getsizeof(testlist)
# print(f"Final size of list: {final_memory_size} bytes")


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = my_list[1::2]
print(result)




