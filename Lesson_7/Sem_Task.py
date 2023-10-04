#Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел. Первое число int, второе -
# float разделены вертикальной чертой. Минимальное число - -1000, максимальное - +1000. Количество строк и имя файла
# передаются как аргументы функции.

from random import randint, uniform


def rnd_num(count, file_name):
    with open(file_name, "a", encoding="utf-8") as f:
        for i in range(count):
            f.write(f'{randint(-1000, 1000)} /{uniform(-1000,1000)} \n')


rnd_num(5, "python part 2\\sem7\\numbers.txt")

#Напишите функцию, которая генерирует псевдоимена. Имя должно начинаться с заглавной буквы, состоять из 4-7 букв,
# среди которых обязательно должны быть гласные. Полученные имена сохраните в файл.

from random import randint
VOWELS = "AEYUIOaeuioy"


def rnd_name():
    name_len = randint(4, 7)
    while True:
        name = ""
        for i in range(name_len):
            name += chr(randint(65, 90))
        for i in name:
            if i in VOWELS:
                return name.capitalize()


def rnd_name_in_file(count, file_name):
    with open(file_name, "a") as f:
        for i in range(count):
            f.write(rnd_name()+"\n")


rnd_name_in_file(5, r"python part 2\sem7\names.txt")

# Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами. Перемножьте пары
# чисел. В новый файл сохраните имя и произведение:
# если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# В результирующем файле должно быть столько же строк, сколько в более длинном файле. При достижении конца более
# короткого файла, возвращайтесь в его начало.

from task15 import rnd_num
from task16 import rnd_name_in_file


def len_list(list1, list2):
    if len(list2) > len(list1):
        temp = len(list1)
    for i in range(len(list2)):
        if i > len(list1) - 1:
            list1.append(list1[i % temp])
        elif len(list2) < len(list1):
            temp = len(list2)
    for i in range(len(list1)):
        if i > len(list2) - 1:
            list2.append(list2[i % temp])
    return list1, list2


def open_file(file_names, file_num, output):
    with (
        open(file_names, 'r') as a,
        open(file_num, 'r') as b,
        open(output, 'w') as c):
        names = a.read().split('\n')
        num = b.read().split('\n')
        for i, j in zip(*len_list(names, num)):
            if j == '':
                continue
        first, second = map(float, j.split('|'))
        mult = first * second
        if mult < 0:
            c.write(f'{i.lower()} {abs(mult)}\n')
        elif mult > 0:
            c.write(f'{i.upper()} {int(mult)}\n')


if __name__ == '__main__':
    rnd_num(10, 'num1.txt')
    rnd_name_in_file(5, 'names1.txt')
    open_file('names1.txt', 'num1.txt', 'output.txt')

# Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:
# расширение
# минимальная длина случайно сгенерированного имени, по умолчанию 6
# максимальная длина случайно сгенерированного имени, по умолчанию 30
# минимальное число случайных байт, записанных в файл, по умолчанию 256
# максимальное число случайных байт, записанных в файл, по умолчанию 4096
# количество файлов, по умолчанию 42
# Имя файла и его размер должны быть в рамках переданного диапазона.

from task16 import rnd_name
from random import randint


def create_files(extension, max_len_name=30, min_len_name=6, min_byte=256, max_byte=4096, qty_file=42):
    for _ in range(qty_file):
        with open(rnd_name() + extension, 'w') as f:
            f.write(str(bytes([randint(0, 255) for _ in range(randint(min_byte, max_byte))])))


if __name__ == '__main__':
    create_files('.txt')

#Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п. Каждая группа включает файлы
# с несколькими расширениями. В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

import os
import pathlib


def sort_files(path):
    os.chdir(path)
    ext = {}
    for i in path.iterdir():
        if i.is_file():
            ext[i.suffix] = ext.get(i.suffix, []) + [i]
    for key, value in ext.items():
        os.mkdir(key)
    for file in value:
        try:
            file.replace(path / key / file.name)
        except PermissionError:
            continue


sort_files(pathlib.Path(r"D:\обучение\python\python part 2\sem7\testt"))