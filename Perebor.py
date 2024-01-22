example1 = [12, 3, 4, 10]
# example1 = [1]
# example1 = []

if len(example1) > 1:
    last_element = example1.pop(-1)
    example1.insert(0, last_element)
else:
    pass
print(example1)

######################################### Variation ############################################################

# example1 = [12, 3, 4, 10]
# example1 = [1]
# example1 = []
#
# if example1:
#     last_element = example1.pop(-1)
#     example1.insert(0, last_element)
# else:
#
#     pass
#
# print(example1)

