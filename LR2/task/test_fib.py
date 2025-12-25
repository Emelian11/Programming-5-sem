from gen_fib import my_genn
from gen_fib import FibonacchiLst

def test_fib_1():
    gen = my_genn()
    assert gen.send(3) == [0, 1, 1], "Тривиальный случай n = 3"


def test_fib_2():
    gen = my_genn()
    assert gen.send(5) == [0, 1, 1, 2, 3], "Пять первых членов ряда"


def test_fib_3():
    gen = my_genn()
    assert gen.send(8) == [0, 1, 1, 2, 3, 5, 8, 13], "Восемь элементов"


def test_fib_zero():
    gen = my_genn()
    assert gen.send(0) == [], "Ноль элементов — пустой список"


def test_fib_one():
    gen = my_genn()
    assert gen.send(1) == [0], "Один элемент"


def test_fib_negative():
    gen = my_genn()
    try:
        gen.send(-5)
        assert False, "Ожидалось исключение ValueError"
    except ValueError:
        pass


def test_multiple_calls():
    gen = my_genn()
    assert gen.send(3) == [0, 1, 1]
    assert gen.send(5) == [0, 1, 1, 2, 3]


if __name__ == "__main__":
    test_fib_1()
    test_fib_2()
    test_fib_3()
    test_fib_zero()
    test_fib_one()
    test_fib_negative()
    test_multiple_calls()
    print("Все тесты успешно пройдены ✔")

if __name__ == "__main__":
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    fib_iter = FibonacchiLst(lst)
    result = list(fib_iter)
    print(f"Числа Фибоначчи из списка {lst}:\n{result}")
