def is_number_prime(number):
    if number % 2 == 0:
        return number == 2
    else:
        divisor = 3
        while divisor * divisor <= number and number % divisor != 0:
            divisor += 2
        return divisor * divisor > number
