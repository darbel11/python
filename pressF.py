import math
import matplotlib.pyplot as plt

ITERATIONS = 20

def my_e(x):
    x_pow = 1
    multiplier = 1
    partial_sum = 1
    for n in range(1, ITERATIONS):
        x_pow *= x  
        multiplier *= 1 / n  
        partial_sum += x_pow * multiplier
    return partial_sum

print ((math.e)**(2))
print (my_e(2))