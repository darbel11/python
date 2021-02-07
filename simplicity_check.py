import random

def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

N = input('Введите число, которое нужно проверить на простоту: ')

if int (N) >= 0 and is_int('{}'.format(N)) is True:
    a = random.randint(1,int(N)-1)
    if (pow(a,int(N)-1,mod = int(N)) == 1):
        print ('Число является простым')
    else:
        print ('Число не является простым')