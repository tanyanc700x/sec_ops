######################### Sets 1 ##############################

x = {1: 1, 2: 2, 3: 3, 4: 4}
y = {2: 22, 3: 33, 5: 55}
merge = {}

z = set(x.keys()).difference(y.keys())
print(z)

common = set(x.keys()).intersection(y.keys())
print(common)


w = {key: x[key] for key in set(x.keys()).difference(y.keys())}
print(w)

merge = {key: [x[key], y[key]] if key in x and key in y else x[key] if key in x else y[key] for key in
         set(x.keys()).union(y.keys())}

print(merge)

################################ Sets 2##################################################


# dict_1 = {1: 1, 2: 2, 3: 3, 4: 4}
# dict_2 = {2: 22, 3: 33, 5: 55}
#
# # а) Створити список із ключів, які є в обох словниках.
# common = dict_1.keys() & dict_2.keys()
# print(common)
#
# # б) Створити список із ключів, які є у першому, але немає у другому словнику.
# absent = dict_1.keys() - dict_2.keys()
# print(absent)
#
# # в) Створити новий словник з пар {ключ:значення} для ключів, які є в першому, але немає в другому словнику.
# pairs = {key: dict_1[key] for key in absent}
# print(pairs)
#
# # г) Об'єднати ці два словники у новий словник за правилом
# merged = {key: [dict_1[key], dict_2[key]] if key in dict_2 else dict_1[key] for key in dict_1.keys()}
# print(merged)
# # print(type(merged))



#####################################################################################################################

# dict_1 = {1: 1, 2: 2, 3: 3, 4: 4}
# dict_2 = {2: 22, 3: 33, 5: 55}
#
# # а) Створити список із ключів, які є в обох словниках
# common_keys = list(dict_1.keys() & dict_2.keys())
#
# # б) Створити список із ключів, які є у першому, але немає у другому словнику.
# keys_only_in_first = list(dict_1.keys() - dict_2.keys())
#
# # в) Створити новий словник з пар {ключ:значення} для ключів, які є в першому, але немає в другому словнику.
# new_dict = {key: dict_1[key] for key in keys_only_in_first}
#
# # г) Об'єднати ці два словники у новий словник за правилом
# merged_dict = {key: [dict_1[key], dict_2[key]] if key in dict_2 else dict_1[key] for key in dict_1.keys()}
#
# # Results
# print("а) Список ключів, які є в обох словниках:", common_keys)
# print("б) Список ключів, які є у першому, але немає у другому словнику:", keys_only_in_first)
# print("в) Новий словник з ключів, які є в першому, але немає в другому словнику:", new_dict)
# print("г) Об'єднаний словник:", merged_dict)
# print("Seems like working")