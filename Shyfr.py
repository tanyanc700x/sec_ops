letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
shyfr = ("хтёиц тц лсдотртжт. тфштжфдшмг хтщфдсисд: ечзмь ёд шфдсяои - сд ёдолдпи емпгьм тымса ёочхсяи. емфм хфдлч "
         "утпцтфд. дзмс си уфдычхцёчиь. зёд смиь. зёд - пмцдпасд, удпцдфд - стфр!")
key = -4
result = ""

for any_char in shyfr:
    if any_char in letters:
        old_char = letters.index(any_char)
        new_char = (old_char + key) % len(letters)   ### OR divmod(old_char + key, len(letters))[1]
        result += letters[new_char]
    else:
        result += any_char
print(result)
#########################################  Another one ################################################

shyfr = ("Не зашифровано")
result = ""
for any_char in shyfr:
    result+= chr(ord(any_char)+key)
    # print(any_char + "  ->  " + str(ord(any_char)))
print(result)

shyfr = result
result = ""

for any_char in shyfr:
    result+= chr(ord(any_char)-key)
print(result)
