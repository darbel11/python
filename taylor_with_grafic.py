import math
import numpy as np
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

#начинаем рисовать графичек

x = np.linspace(0, 3*np.pi, 100)
y1 = my_e(x)
y2 = np.exp(x)

fig, ax = plt.subplots()

ax.plot(x, y1,
        color = 'violet',
        linewidth = 7)

ax.plot(x, y2,
        color = 'blue',
        linewidth = 2)

ax.minorticks_on()

ax.grid(which='major',
        color = 'k',
        linewidth = 0.5)

ax.grid(which='minor',
        color = 'k',
        linewidth = 0.1)

plt.show()