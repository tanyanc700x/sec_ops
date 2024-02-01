def sentence_correction(text):
    sentences = text.split('. ')
    corrected_sentences = [sentence.capitalize() for sentence in sentences]
    corrected_text = '. '.join(corrected_sentences)

    # Dot at the end
    if not corrected_text.endswith('.'):
        corrected_text += '.'

    return corrected_text

# Тести
assert sentence_correction("greetings, friends") == "Greetings, friends.", 'Test1'
assert sentence_correction("hello") == "Hello.", 'Test2'
assert sentence_correction("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert sentence_correction("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert sentence_correction("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
