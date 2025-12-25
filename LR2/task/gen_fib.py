import functools


def my_genn():

    result = None
    while True:
        n = yield result

        if n < 0:
            raise ValueError("n must be >= 0")

        a, b = 0, 1
        result = []
        for _ in range(n):
            result.append(a)
            a, b = b, a + b


def fib_coroutine(func):
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return wrapper


my_genn = fib_coroutine(my_genn)


class FibonacchiLst:
    def __init__(self, instance):
        self.instance = instance
        self.idx = 0

    def __iter__(self):
        return self

    def __is_fib(self, n):
        if n < 0:
            return False


        def is_square(x):
            s = int(x ** 0.5)
            return s * s == x

        return is_square(5 * n * n + 4) or is_square(5 * n * n - 4)

    def __next__(self):
        while True:
            if self.idx >= len(self.instance):
                raise StopIteration

            value = self.instance[self.idx]
            self.idx += 1

            if self.__is_fib(value):
                return value