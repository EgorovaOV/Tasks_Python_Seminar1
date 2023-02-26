#Программа загадывает число от 0 до 1000.
# Необходимо угадать число за 10 попыток. Программа должна
#подсказывать “больше” или “меньше” после каждой попытки.
#Для генерации случайного числа используйте код:
#from random import randint
#num = randint(LOWER_LIMIT, UPPER_LIMIT)

print('Попробуй угадать число')

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
print(num)

MAX_COUNT = 10

count = 1
while count <= MAX_COUNT:
    print('Попытка номер ', count)
    a = int(input('Введи число от 0 до 1000 '))
    if a > num:
        print('попробуй число поменьше')
        count += 1
    elif a < num:
        print('попробуй число побольше')
        count += 1
    else:
        print('Ты угадал')
        break


