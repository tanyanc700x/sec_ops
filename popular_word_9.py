def popular_words(text, words):

    counting_words = {word: text.lower().split().count(word) for word in words}
    # print(counting_words)

    return counting_words


 # Пример использования
assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')
