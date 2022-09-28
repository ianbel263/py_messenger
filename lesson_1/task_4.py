# Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
# и выполнить обратное преобразование (используя методы encode и decode).

words = ['разработка', 'администрирование', 'protocol', 'standard']

words_unicode = [word.encode('utf-8') for word in words]
words_str = [word.decode('utf-8') for word in words_unicode]

print('До преобразования: ', words)
print('После преобразования в UNICODE: ', words_unicode)
print('После обратного преобразования: ', words_str)
