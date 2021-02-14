import random


def checking(n: int) -> bool:
    if n >= 0:
        a = random.randint(1, int(n) - 1)
        if pow(a, int(n) - 1, mod=int(n)) == 1:
            # print('Число является простым')
            return True
        else:
            # print('Число не является простым')
            return False


checking(int(input('Введите число, которое нужно проверить на простоту: ')))
