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

# Вывод результата
print(result)
