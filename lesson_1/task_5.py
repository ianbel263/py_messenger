# Выполнить пинг веб-ресурсов yandex.ru, youtube.com
# и преобразовать результаты из байтовового в строковый тип на кириллице


import locale
import platform
import subprocess

PING_COUNT = '2'
resources = ['yandex.ru', 'youtube.com']

param = '-n' if platform.system().lower() == 'windows' else '-c'
default_encoding = locale.getpreferredencoding()

for resource in resources:
    args = ['ping', param, PING_COUNT, resource]
    process = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in process.stdout:
        line = line.decode(default_encoding)
        print(line)
