alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
encrypt = ("хтёиц тц лсдотртжт. тфштжфдшмг хтщфдсисд. ечзмь ёд шфдсяои, сд ёдолдпи емпгьм тымса ёочхсяи. емфм хфдлч утпцтфд. дзмс си уфдычхцёчиь. зёд смиь. зёд - пмцдпасд, удпцдфд - стфр!")
key = -4
encrypt = encrypt.lower()
encrypted = ""

for my_char in encrypt:
    if my_char  in alphabet:
        position = alphabet.index(my_char )
        newPosition = (position + key) % len(alphabet)
        encrypted += alphabet[newPosition]
    else:
        encrypted += my_char

print("Зашифрованный текст:", encrypted)
