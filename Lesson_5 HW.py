#EASY
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
# Учесть проверку на то что папка не пуста и на то, что такая папка уже существует

import os
# for n in range(1, 10):
#     dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(n))
#     try:
#         os.mkdir(dir_path)
#     except FileExistsError:
#         print("Директория уже есть")
for n in range(1, 10):
    dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(n))
    try:
        os.rmdir(dir_path)
    except:
        print("Папка {} удалена или не пустая".format(dir_path))


# Задача-2:
# Напишите скрипт, который выводит в консоль список файлов и папок в указанной директории.
# for i in os.listdir("."):
#     print(i)



#NORMAL

# Написать две программы:
# Одна принимает через argparse число N и текст S и в цикле N раз выводит S в консоль
# А вторая программа принимает через input число M
# И указанное кол-во раз спрашивает через input N и S и запускает первую программу через os.system

# import sys
# first:
# os.system('Test.py 3 Hi')

# second
# m = int(input())
# for i in range(m):
#     n = input('Введите число: ')
#     s = input('Введите строку: ')
#     os.system('Test.py {} {}'.format(n, s))

#HARD

# Написать программу для распаковки файлов в корневую из всех папок с расширениями (код взять с урока) и папки удалить
# Скрипт ходит по всем папкам текущей директории и вытаскивает вложенные на один уровень файлы в корневую.


# for i in os.listdir(os.getcwd()):
#     if os.path.isdir(i):
#         for j in os.listdir(os.path.join(os.getcwd(), i)):
#             if os.path.isfile(os.path.join(os.getcwd(), i, j)):
#                 os.rename(os.path.join(os.getcwd(), i, j), os.path.join(os.getcwd(), j))


