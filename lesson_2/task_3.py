# 3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в файле
# YAML-формата. Для этого:
# Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число,
# третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим
# в кодировке ASCII (например, €);
# Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию файла
# с помощью параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;
# ВАЖНО: Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.

import yaml


def write_data_to_yaml(file, data):
    with open(file, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)


filename = 'file.yaml'
data = {
    'list': ['Молоко', 2, 99, 'Petrov', '19.01.2022'],
    'int': 336,
    'dict': {
        'price_1': '100€',
        'price_2': '100£',
        'price_3': '100₽',
        'price_4': '100¥',
    }
}

write_data_to_yaml(filename, data)

with open(filename, encoding='utf-8') as f:
    file_data = yaml.load(f, Loader=yaml.FullLoader)

if data == file_data:
    print('Исходные и загруженные данные совпадают')
else:
    print('Исходные и загруженные данные не совпадают')
