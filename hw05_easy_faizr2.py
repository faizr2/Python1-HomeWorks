import os
import sys
import shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def my_mkdir():
    k = 1
    while k < 10:
        try:
            os.mkdir("dir_{}".format(k))
            print ('Папка создана')
        except FileExistsError:
            print ('Папка уже существует')
        k+=1

def my_deldir():
    j = 1
    while j < 10:
        try:
            os.rmdir("dir_{}".format(j))
            print ('Папка удалена')
        except FileNotFoundError:
            print ('Папка не существует')
        j+=1

my_mkdir()
my_deldir()


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def my_listdir():
    try:
        print ('Список директорий в текущем каталоге:')
        list_dir = os.listdir(".")
        for dir_ in list_dir:
            is_dir = os.path.isdir(dir_)
            if is_dir:
                print (dir_)
    except FileExistsError:
        print("Ошибка")
        
my_listdir()


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого
# запущен данный скрипт.


import shutil

def current_file_copy():
    name_file = os.path.realpath(__file__)
    new_file = name_file +'.copy'
    if os.path.isfile(new_file) != True:
        shutil.copy(name_file, new_file)
        return new_file + ' - создан'
    else:
        return 'Файл давно скопирован'

print(current_file_copy())
