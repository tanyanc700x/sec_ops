alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
shyfr = ("хтёиц тц лсдотртжт. тфштжфдшмг хтщфдсисд. ечзмь ёд шфдсяои, сд ёдолдпи емпгьм тымса ёочхсяи. емфм хфдлч "
         "утпцтфд. дзмс си уфдычхцёчиь. зёд смиь. зёд - пмцдпасд, удпцдфд - стфр!")
key = -4
result = ""

for any_char in shyfr:
    if any_char in alphabet:
        position = alphabet.index(any_char)
        newPosition = (position + key) % len(alphabet)
        result += alphabet[newPosition]
    else:
        result += any_char

print(result)


