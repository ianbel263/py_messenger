# Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
# соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode
# и также проверить тип и содержимое переменных

words = {
    'str': ['разработка', 'сокет', 'декоратор'],
    'utf-8': [
        '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
        '\u0441\u043e\u043a\u0435\u0442',
        '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
    ]
}


def get_type(var):
    return {
        'content': var,
        'type': type(var)
    }


for value in words.values():
    for word in value:
        print(get_type(word))