example1 = [12, 3, 4, 10]
if example1:
    last_element = example1.pop(-1)
    example1.insert(0, last_element)

example2 = [1]
if example2:
    last_element = example2.pop(0)  # or example2.pop(-1)
    example2.insert(0, last_element)

example3 = []
if example3:
    last_element = example3.pop(-1) #I think can be done in many ways since the list is empty.Maybe this check is not
    # necessayat all.
    example3.insert(0, last_element)
# example3 = []
# if example3:
#     example3.insert(0, example3.pop())
print(example1)  # [10, 12, 3, 4]
print(example2)  # [1]
print(example3)  # []

############################################### Different way##############################################


example1 = [12, 3, 4, 10]
iterations = 4

for _ in range(iterations):
    last_element = example1.pop(0)
    example1.append(last_element)
    print(example1)

print("Cool! Magic!")
