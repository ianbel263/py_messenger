# Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность
# кодов (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.


words = ['class', 'function', 'method']


def convert_word(val):
    return eval(f'b"{val}"')


def get_data(val):
    return {
        'content': val,
        'type': type(val),
        'length': len(val)
    }


for word in words:
    print(get_data(word))
    print(get_data(convert_word(word)))
    print('---------------------')
