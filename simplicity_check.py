a = int(input())

def prime(a):
    b = 3
    while a % b != 0:
        b+=1
    return a == b
print (prime(a))