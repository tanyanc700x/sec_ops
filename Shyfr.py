letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
shyfr = ("хтёиц тц лсдотртжт. тфштжфдшмг хтщфдсисд: ечзмь ёд шфдсяои - сд ёдолдпи емпгьм тымса ёочхсяи. емфм хфдлч "
         "утпцтфд. дзмс си уфдычхцёчиь. зёд смиь. зёд - пмцдпасд, удпцдфд - стфр!")
key = -4
result = ""

for any_char in shyfr:
    if any_char in letters:
        char_place = letters.index(any_char)
        char_place_2 = (char_place + key) % len(letters)
        result += letters[char_place_2]
    else:
        result += any_char

print(result)


