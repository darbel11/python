from import_modul1 import is_number_prime
user_input = int(input('Введите значение: '))
simplicity = is_number_prime(user_input)

if simplicity:
    print('Введенное число {} простое'.format(user_input))
else:
    print('Введенное число {} составное'.format(user_input))
