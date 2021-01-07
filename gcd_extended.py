a = int(input())
b = int(input())

def gcd_ex(a, b):
    if b == 0:
        return a, 1, 0
    else:
        c, x, y = gcd_ex(b, a % b)
        return c, y, x - (a//b)*y
print (gcd_ex(a, b))