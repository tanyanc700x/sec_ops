example1 = [12, 3, 4, 10]
if example1:
    last_element = example1.pop(-1)
    example1.insert(0, last_element)

example2 = [1]
if example2:
    last_element = example2.pop(0)  # or example2.pop(-1) but may be it will be a type of redundancy. HZ.
    example2.insert(0, last_element)

example3 = []
if example3:
    last_element = example3.pop(-1) #I think it can be done in many ways since the list is empty. Maybe this check is
    # not necessay at all.
    example3.insert(0, last_element)
# example3 = []
# if example3:
#     example3.insert(0, example3.pop())
print(example1)  # [10, 12, 3, 4]
print(example2)  # [1]
print(example3)  # []

############################################### Better way ##############################################


# example1 = [12, 3, 4, 10]
# example2 = [1]
# example3 = []
# iterations = 4
#
# for _ in range(iterations):
#     last_element = example1.pop(0)
#     example1.append(last_element)
#     print(example1)
#     print(example2)
#     print(example3)
#
# example1.sort()
# print(example1)
# example1.sort(reverse=True)
# print(example1)


##################################################Playground with lists################################################


# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))
# print(thislist)
#
# list1 = ["apple", "banana", "cherry"]
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]
# print(type(list1))
# print(type(list2))
# print(type(list3))
# print(list1[2])
#
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])
# print(thislist[:4])
# print(thislist[-6:-3])
#
#
# thislist = ["apple", "banana", "cherry"]


# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# thislist[0] = 12
# print(thislist)
#
# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)

# fruits = ['apple', 'banana', 'cherry', 'orange']
# x = fruits.copy()
# fruits.append(x)
# y = x
# fruits.append(y)
# print(fruits)
# print(len(fruits))
# if fruits:
#     last_element = fruits.pop(-1)
#     fruits.insert(0, last_element)
#     print(fruits)

# iterations = 6
#
# for _ in range(iterations):
#     last_element = fruits.pop(0)
#     fruits.append(last_element)
#     print(fruits)
#
# yx = fruits.count("cherry")
# print(yx)


# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list1.extend(list2)
# print(list1)