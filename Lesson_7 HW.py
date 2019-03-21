Задание-1
Есть два игрока и 25 монет.
Каждый может брать от 1 до 3 монет.
Проигрывает тот кто забрал последнюю.

Написать программу для этой игры

import random
coins = 25
player = 1

while coins >0:
    i = random.randint(1, 3)
    if i > coins:
        i = coins
    coins -= i
    print("{} player: {} coins, all = {} coins".format(player, i, coins ))

    if player == 1:
        player = 2
    else:
        player = 1
print('{} player is win!'.format(player))


Задание-2
Написать функцию для записи значений словаря в файл
например
{
    "Name":[3,1,2,3,4],
    "Surname":[3,4,5,6,7,8],
    "Fathername":[3,4,5,6,7,8]
}
т.е. в данном случае создастся три файла name, surname, fathername и внутри на каждой отдельной строке значения из массива


dic = {
    "Name":[3,1,2,3,4],
    "Surname":[3,4,5,6,7,8],
    "Fathername":[3,4,5,6,7,8]
}
for keys in dic:
    f = open(keys + '.txt', 'w')
    for i in dic[keys]:
        f.write(str(i) + '\n')
