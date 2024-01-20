########################################## While loop #############################################################
listik = [0, 1, 0, 12, 3]
# listik = [0]
# listik = [1, 0, 13, 0, 0, 0, 5]
# listik = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
while True:
    if len(listik) > 1:
        result = [x for x in listik if x != 0] + [x for x in listik if x == 0]
        break
    else:
        result = listik
        break

print(result)

##########################################  Ternary operator in use  #####################################################

# listik = [0, 1, 0, 12, 3]
# listik = [0]
# listik = [1, 0, 13, 0, 0, 0, 5]
# listik = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
# result = [x for x in listik if x != 0] + [x for x in listik if x == 0] if len(listik) > 1 else listik
# print(result)


