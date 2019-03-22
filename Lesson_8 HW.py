# Правила игры в лото.
# Игра ведется с помощью специальных карточек, на которых отмечены числа,
# и фишек (бочонков) с цифрами.
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
# --------------------------
#     9 43 62          74 90
#  2    27    75 78    82
#    41 56 63     76      86
# --------------------------
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
# случайная карточка.
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
#     Если цифра есть на карточке - она зачеркивается и игра продолжается.
#     Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
#     Если цифра есть на карточке - игрок проигрывает и игра завершается.
#     Если цифры на карточке нет - игра продолжается.
#
# Побеждает тот, кто первый закроет все числа на своей карточке.
# Пример одного хода:
# Новый бочонок: 70 (осталось 76)
# ------ Ваша карточка -----
#  6  7          49    57 58
#    14 26     -    78    85
# 23 33    38    48    71
# --------------------------
# -- Карточка компьютера ---
#  7 11     - 14    87
#       16 49    55 77    88
#    15 20     -       76  -
# --------------------------
# Зачеркнуть цифру? (y/n)
import random

mylist = []
myNums = []

def MyList():
    mylist = [i for i in range(1,91)]
    return mylist
def MyNums():
    mylist = MyList()
    for n in range(15):
        nums = random.choice(mylist)
        mylist.remove(nums)
        myNums.append(nums)
    return myNums

def listIndex():
    lineIndex = []
    myIndex = [i for i in range(9)]
    for j in range(5):
        index = random.choice(myIndex)
        myIndex.remove(index)
        lineIndex.append(index)
    return lineIndex

def PrintCards():
    print('Выпал бочонок {}, осталось:{}'.format(bochonok, len(mylist)), '\n')
    print('----Ваша карточка----')
    for line in cards[0]:
        print(*line)
    print('---------------------')
    print('----Карточка компьютера', '\n')
    for line in cards[1]:
        print(*line)
    print('---------------------')
# формируем карточки
myCard = []
pcCard = []
cards = [myCard, pcCard]

i = 0
for el in cards:
    cards[i] = [[' ' for j in range(9)] for i in range(3)]
    myNums = MyNums()
    for line in range(3):
        index = 0
        LineIndex = listIndex()
        for index in range(9):
            if index in LineIndex:
                n = random.choice(myNums)
                myNums.remove(n)
                cards[i][line][index] = n
    i += 1

#начинаем игру
def NumberExist(bochonok,cards):
    if bochonok in cards[0]:
        return [0,cards[0].index(bochonok)]
    elif bochonok in cards[1]:
        return [1, cards[1].index(bochonok)]
    elif bochonok in cards[2]:
        return [2,cards[2].index(bochonok)]

mylist = MyList()
myOst = 15
compOst = 15
while len(mylist) > 0:
    bochonok = random.choice(mylist)
    mylist.remove(bochonok)
    PrintCards()
    ans = input('Продолжить или зачеркнуть номер? (y / n)')
    if ans == 'y':
        #Цифра есть:
        # зачеркиваем свою
        if not NumberExist(bochonok, cards[0]) == None:
            cards[0][(NumberExist(bochonok, cards[0])[0])][(NumberExist(bochonok, cards[0])[1])] = '-'
            myOst -= 1
            print('Не закрыто у тебя:', myOst)
            if myOst == 0:
                print('Ты выиграл!')
                break
        else:
            print('Ты проиграл!')
            break
    elif ans == 'n':
        if NumberExist(bochonok, cards[0]):
            print('Ты проиграл!')
            break
    else:
        ans = input('Продолжить или зачеркнуть номер? (y / n)')
    # в конце проверка номера в карточке компьютера
    if not NumberExist(bochonok, cards[1]) == None:
        cards[1][(NumberExist(bochonok, cards[1])[0])][(NumberExist(bochonok, cards[1])[1])] = '-'
        compOst -= 1
        print('Не закрыто у компьютера:', compOst)
        if compOst == 0:
            print('Компьютер выиграл!')
            break






