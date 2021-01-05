import numpy as np

from numpy.linalg import solve as solve_out_of_the_box
from numpy import array
from numpy.linalg import norm

ab = array([
    [1.5, 2.0, 1.5, 2.0, 5.0],
    [3.0, 2.0, 4.0, 1.0, 6.0],
    [1.0, 6.0, 0.0, 4, 7.0],
    [2.0, 1.0, 4.0, 3, 8.0]
], dtype=float)


def vector_gauss(ab):
    n = ab.shape[0]

    for k in range(n - 1):
        for i in range(k + 1, n):
            frac = ab[i, k] / ab[k, k]
            ab[i, :] -= ab[k, :] * frac

    x = np.matrix([0.0 for i in range(n)]).T
    for k in range(n - 1, -1, -1):
        x[k, 0] = (ab[k, -1] - ab[k, k:n] * x[k:n, 0]) / ab[k, k]

    x = ab[:, -1]
    return x


a = array([
    [1.5, 2.0, 1.5, 2.0],
    [3.0, 2.0, 4.0, 1.0],
    [1.0, 6.0, 0.0, 4],
    [2.0, 1.0, 4.0, 3]
], dtype=float)

b = array([5, 6, 7, 8], dtype=float)

solution = vector_gauss(ab)
oob_solution = solve_out_of_the_box(a, b)

print(solution)
print("Максимальное отклонение компоненты решения:", norm(solution - oob_solution, ord=1))