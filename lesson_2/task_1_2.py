# Другой способ

import csv
import re
from pathlib import Path

from chardet import detect


def get_data(files):
    if len(files) < 1:
        return []
    result = []
    headers = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    for file in files:
        with open(file, 'rb') as f:
            content = f.read()
        encoding = detect(content)['encoding']
        data = {}
        with open(file, encoding=encoding) as f:
            for line in f:
                line = line.rstrip()
                for header in headers:
                    if re.match(header, line):
                        data[header] = re.search(fr'({header}).\s*(.*)', line).group(2)
                        break
        result.append(data)
    return result


def write_to_csv(filename, files):
    data = get_data(files)
    with open(filename, 'w', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=list(data[0].keys()))
        writer.writeheader()
        writer.writerows(data)


CSV_FILENAME = 'computers.csv'
INITIAL_DIR_PATH = 'initial_data'
INITIAL_FILENAME_MASK = 'info_*.txt'

paths = sorted(Path(INITIAL_DIR_PATH).glob(INITIAL_FILENAME_MASK))
write_to_csv(CSV_FILENAME, paths)
