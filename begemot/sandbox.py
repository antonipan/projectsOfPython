import random


def input_text():
    msg = input()
    return msg

def random_joke():
    with open('zodiac.txt', 'r') as data:
        somelist = list(data.readlines())
        some_el = somelist[random.randint(0, len(somelist)-1)]
        some_el = some_el.rstrip('\n')
        print(some_el)
# random_joke()


def guess_number():
    m = random.randint(1,1000)
    n = int(input('Компьютер загадал число. Выбери количество попыток, чтобы отгадать: '))
    k = None
    while k != m and n > 0:
        print(f'Осталось попыток - {n}')
        k = int(input('Введите число: '))
        check_num(m, k)
        if k == m:
            print('Вы угадали!')
        n -=1
    if n == 0:
        print(f'Вы исчерпали все попытки. Загадано число {m}')

def check_num(m, k):
    if k < m:
        print('Двигайся вправо!')
    elif k > m:
        print('Двигайся влево!')



def trow_bone():
    m = int(input('Введи количество попыток: '))
    level = int(input('Выбери уровень: 1 - лёгкий, 2 - средний, 3 - сложный: '))
    some_list = [8, 4, 1]
    x = some_list[level-1]
    coincidence = 0
    while m > 0 or coincidence == 3:
        y = None
        print(f'Осталось попыток: {m}')
        user_bone1 = int(input('Введи число: '))
        while x > 0:
            y = False
            rand_bone = random.randint(1,6)
            if user_bone1 == rand_bone:
                coincidence +=1
                print(f'Ура, кости совпали:  ваше число - {user_bone1}, число компьютера - {rand_bone}')
                y = True
                break
            x -= 1
        if y == False:
            print('Увы. Не совпало')
            print(f'Ваше число - {user_bone1}, число компьютера - {rand_bone}')
        x = some_list[level-1]
        m -=1
    if coincidence < 3:
        print('Увы. Сегодня не твой день')
        print(f'Количество совпадений: {coincidence}')
    else:
        print(f'Круто. Количество совпадений: {coincidence}')


trow_bone()

# guess_number()