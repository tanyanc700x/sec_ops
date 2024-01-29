# sentence = input("Введите рядок:" )
# literal = '''!"#$%&'()*+,  -./:;<=>?@[\\]^`{|}~'''
# kwlist = "False", "await", "else", "import", "pass", "None", "break", "except", "in", "raise", "True", "class", "finally", "is", "return", "and", "continue", "for", "lambda", "try", "as", "def", "from", "nonlocal", "while", "assert", "del", "global", "not", "with", "async", "elif", "if", "or", "yield"
# # result = ""
# for char in sentence:
#     if literal in sentence:
#         result = "False"
#
#     if sentence.startswith(kwlist[::]):
#         result = "False"
#     elif sentence[0].isdigit():
#         result = "False"
#     elif not sentence.islower():
#             result = "False"
#     elif not sentence.isalnum():
#             result = "False"
#
#     elif sentence.find("_")>1:
#         result = "False"
#     else:
#         result = "True"
# print(result)

#################################
# sentence = input("Введите рядок: ")
# literal = '''!"#$%&'()*+,  -./:;<=>?@[\\]^`{|}~'''
# kwlist = ["False", "await", "else", "import", "pass", "None", "break", "except", "in", "raise", "True", "class", "finally", "is", "return", "and", "continue", "for", "lambda", "try", "as", "def", "from", "nonlocal", "while", "assert", "del", "global", "not", "with", "async", "elif", "if", "or", "yield"]
#
# result = "True"
#
# if any(char.isupper() or char.isspace() or char in literal for char in sentence):
#     result = "False"
# if sentence in kwlist:
#     result = "False"
# if sentence[0].isdigit():
#     result = "False"
#
# if len(sentence) == 1 and sentence == "_":
#     result = "True"
# elif "_" in sentence and (sentence.startswith("_") or sentence.endswith("_")):
#     result = "False"
#
# # Вывод результата
# print(result)
###########################################################

sentence = input("Введите рядок: ")
literal = '''!"#$%&'()*+,  -./:;<=>?@[\\]^`{|}~'''
kwlist = ["False", "await", "else", "import", "pass", "None", "break", "except", "in", "raise", "True", "class",
          "finally", "is", "return", "and", "continue", "for", "lambda", "try", "as", "def", "from", "nonlocal",
          "while", "assert", "del", "global", "not", "with", "async", "elif", "if", "or", "yield"]

result = "True"

# Проверка наличия больших букв, пробелов, спецсимволов и зарезервированных слов
for char in sentence:
    if char.isupper() or char.isspace() or char in literal:
        result = "False"
        break # поставила его тут на случай,  позволяет прервать цикл, как только найден первый символ,
        # который соответствует одному из условий: является заглавной буквой, пробелом или принадлежит
        # к множеству спецсимволов literal.

# Проверка на зарезервированные слова
if sentence in kwlist:
    result = "False"

# Проверка на начало с числа
if sentence[0].isdigit():
    result = "False"

# # Проверка на нижнее подчеркивание как отдельный символ
# if len(sentence) == 1 and sentence == "_":
#     result = "True"
# elif "_" in sentence and (sentence.startswith("_") or sentence.endswith("_")):
#     result = "True"

# Вывод результата
print(result)
