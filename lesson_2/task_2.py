# 2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
# Написать скрипт, автоматизирующий его заполнение данными. Для этого:
# Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
# цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл
# orders.json. При записи данных указать величину отступа в 4 пробельных символа;
# Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.

import json


def write_order_to_json(item, quantity, price, buyer, date):
    filename = 'orders.json'
    dict_to_json = {}
    try:
        with open(filename, encoding='utf-8') as f:
            dict_to_json = json.load(f)
    except FileNotFoundError:
        dict_to_json['orders'] = []
    dict_to_json['orders'].append({
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date,
    })
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(dict_to_json, f, indent=4, ensure_ascii=False)


write_order_to_json('Молоко', 2, 99, 'Петров', '19.01.2022')
write_order_to_json('Кефир', 4, 66, 'Сидоров', '22.03.2022')
write_order_to_json('Хлеб', 2, 22, 'Иванов', '05.05.2022')
write_order_to_json('Колбаса', 1, 490, 'Пупкин', '08.09.2022')
