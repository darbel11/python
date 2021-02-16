
print ( 'Input one number' )
print()
a = int (input () )

def isNumberPrime(n):
    if n % 2 == 0:
        return n == 2
    else:
        x = 3
        while x * x <= n and n % x != 0:
            x += 2
        return x * x > n

b = isNumberPrime(a)
print()
print(a, 'Is prime number:',b)