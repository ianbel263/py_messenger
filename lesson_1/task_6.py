# Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
# Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое

from chardet import detect

filename = 'test_file.txt'
words = ['сетевое программирование', 'сокет', 'декоратор']

with open(filename, 'w') as f:
    for word in words:
        print(word, file=f)

with open(filename, 'rb') as f:
    content = f.read()
encoding = detect(content)['encoding']
print(f'Encoding file {filename} is', encoding)

print('-------------------------------------')

with open(filename, encoding='utf-8') as f:
    for line in f:
        print(line, end='')

# Тут не совсем понял задание - сделал, как написано дословно. Однако этот код не будет работать на Windows, так как
# запишет файл в кодировке Windows-1251, соответственно открыть его в Unicode не сможет
