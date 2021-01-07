import numpy as np

from numpy.linalg import solve as solve_out_of_the_box
from numpy import array
from numpy.linalg import norm

a = array([
    [1.5, 2.0, 1.5, 2.0],
    [3.0, 2.0, 4.0, 1.0],
    [1.0, 6.0, 0.0, 4],
    [2.0, 1.0, 4.0, 3]
], dtype = float)

b = array([5, 6, 7, 8], dtype = float)

d = len(a)

def vector_gauss(a, b):
    a = a.copy()
    b = b.copy()

    for j in range(d - 1):
        for i in range(j + 1, d):
            frac = a[i, j] / a[j, j]
            a[i, j + 1:d] -= a[j, j + 1:d] * frac
            b[i] = b[i] - frac * b[j]

    for k in range(d - 1, -1, -1):
        b[k] = (b[k] - np.dot(a[k, k + 1:d], b[k + 1:d])) / a[k, k]
    return b

solution = vector_gauss(a, b)
oob_solution = solve_out_of_the_box(a, b)

print(solution)
print("Максимальное отклонение компоненты решения:", norm(solution - oob_solution, ord=1))