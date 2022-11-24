# Создайте программу для игры с конфетами человек против человека. 
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# б) Подумайте, как наделить бота "интеллектом"

# Для двух игроков:
from random import randint

def inputCandies(st):
    number =int(input(f"Введите количество конфет (от 1 до {st}): "))
    while number < 1 or number > 28:
        number =int(input(f"Введите количество конфет (от 1 до {st}): "))
    return number

def game(st, candies, queue):    
    if queue: 
        candies-=inputCandies(st)
        queue = 0
    else:
        print('ход бота')
        candies-=randint(1,st)
        queue = 1
    return candies, queue

def rnS():
    st = randint(5,30)
    return st 

def rnQC(rc):
    qua = randint((rc*2+1),2500)
    return qua


queue =randint(0,2)
step =rnS()
candies= rnQC(step)
print(f'Всего {candies} конфет')
while (candies>0):
    candies, queue=game(step, candies, queue)
    print(f'Осталось {candies} конфет')

if queue:
    print ('Выиграл player2')
else:
    print ('Выиграл player1')