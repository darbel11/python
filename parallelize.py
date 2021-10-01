import multiprocessing
import random
import time


def point_generation():
    generator = random.Random()
    x, y = generator.random(), generator.random()

    return x, y


def point_generation_wrapper(_):
    return point_generation()


def checker(point):
    x, y = point
    if x ** 2 + y ** 2 <= 1:
        return 1


if __name__ == '__main__':
    MESSAGE = 'Введите число (точность вычислений будет зависеть от этого числа): '
    amount_of_points = int(input(MESSAGE))

    start_time = time.time()

    with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
        points = pool.map(func=point_generation_wrapper, iterable=[0] * amount_of_points)
        check_results = pool.map(func=checker, iterable=points)

    points_inside_the_area = 0
    for result in check_results:
        if result:
            points_inside_the_area += 1

    calculated_pi = points_inside_the_area / amount_of_points * 4

    print('Calculated value of PI:', calculated_pi, sep=' ')
    print('Operating time: ', time.time() - start_time, sep=' ')

else:
    print(__name__)
