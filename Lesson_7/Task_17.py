# Напишите функцию группового переименования файлов. Она должна:
# - принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из
# исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os

def batch_rename(new_name, digits, source_ext, dest_ext, range_name, path='.'):
    count = 1
    for filename in os.listdir(path):
        if filename.endswith(source_ext):
            # получаем имя без расширения
            old_name = os.path.splitext(filename)[0]
            # получаем часть стагоро имени в заданом диапазоне или оставляем пустым
            old_name_substring = old_name[range_name[0]-1:range_name[1]] if range_name else ""
            # создаем новое имя файла из части старого + новое + порядковый номер в 3х значном представлении + расширение
            new_filename = f"{old_name_substring}{new_name}{str(count).zfill(digits)}{dest_ext}"
            #переименуем файл
            os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
            count += 1

batch_rename('new_file', 3, '.txt', '.md', [3, 6], r"..\Lesson_7")
