# Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

words = ['attribute', 'класс', 'функция', 'type']


def is_convert(val):
    try:
        val.encode('ascii')
    except UnicodeEncodeError:
        return False
    else:
        return True


for word in words:
    result = 'можно' if is_convert(word) else 'нельзя'
    print(f'Слово "{word}" {result} преобразовать в кодировку ASCII')
