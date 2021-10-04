def is_number_prime(number):
    if number % 2 == 0:
        return number == 2
    else:
        divisor = 3
        while divisor * divisor <= number and number % divisor != 0:
            divisor += 2
        return divisor * divisor > number


if __name__ == '__main__':
    user_input = int(input('Input integer: '))
    simplicity = is_number_prime(user_input)

    if simplicity:
        print('Inputed number {} is prime'.format(user_input))
    else:
        print('Inputed number {} isn\'t prime'.format(user_input))
