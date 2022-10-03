# 1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из
# файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:
# Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и
# считывание данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь
# значения параметров «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра
# поместить в соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list,
# os_code_list, os_type_list. В этой же функции создать главный список для хранения данных отчета — например,
# main_data — и поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС»,
# «Код продукта», «Тип системы». Значения для этих столбцов также оформить в виде списка и поместить в
# файл main_data (также для каждого файла);
# Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение
# данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
# Проверить работу программы через вызов функции write_to_csv().

import csv
import re
from pathlib import Path

from chardet import detect


def get_data(files):
    if len(files) < 1:
        return []
    result = []
    main_data = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    name_to_arrays = {
        'Изготовитель системы': os_prod_list,
        'Название ОС': os_name_list,
        'Код продукта': os_code_list,
        'Тип системы': os_type_list,
    }
    for i in range(len(files)):
        with open(files[i], 'rb') as f:
            content = f.read()
        encoding = detect(content)['encoding']
        with open(files[i], encoding=encoding) as f:
            for line in f:
                line = line.rstrip()
                for key, arr in name_to_arrays.items():
                    if re.match(key, line):
                        arr.append(re.search(fr'({key}).\s*(.*)', line).group(2))
                        break
        result.append([
            os_prod_list[i], os_name_list[i], os_code_list[i], os_type_list[i]
        ])
    return [
        main_data, *result,
    ]


def write_to_csv(filename, files):
    data = get_data(files)
    with open(filename, 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(data)


CSV_FILENAME = 'computers.csv'
INITIAL_DIR_PATH = 'initial_data'
INITIAL_FILENAME_MASK = 'info_*.txt'

paths = sorted(Path(INITIAL_DIR_PATH).glob(INITIAL_FILENAME_MASK))
write_to_csv(CSV_FILENAME, paths)
