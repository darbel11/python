import itertools


class Fib:
    class _Fib_iter:
        def __init__(self):
            self.fib1 = 0
            self.fib2 = 1

        def __next__(self):
            a = self.fib1
            self.fib1 = self.fib2
            self.fib2 = self.fib2 + a
            a = self.fib1
            return a

    def __iter__(self):
        return Fib._Fib_iter()


print(list(itertools.islice(Fib(), 90)))