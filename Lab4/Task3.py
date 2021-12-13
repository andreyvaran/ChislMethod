import sympy
import matplotlib.pyplot as plt
import numpy as np
from threading import Thread
from math import *
import numba
from sympy.plotting import plot

x = sympy.Symbol('x')


def runge(func, a, b, eps) -> int:
    n = 5
    n2 = 2 * n + 1

    h = (b - a) / n
    lst = [a + h * i for i in range(n + 1)]

    h2 = (b - a) / n
    lst2 = [a + h2 * i for i in range(n + 1)]
    while abs(midl_sq(func, lst2, h2) - midl_sq(func, lst, h)) > (1/3)*eps:
        print(n)
        n += 2
        n2 = 2 * n + 1

        h = (b - a) / n
        lst = [a + h * i for i in range(n + 1)]

        h2 = (b - a) / n
        lst2 = [a + h2 * i for i in range(n + 1)]
    return n

def midl_sq(func, iter_lst, h):
    res = 0
    for i in range(1, len(iter_lst)):
        res += func.subs(x, ((iter_lst[i] + iter_lst[i - 1]) / 2)).evalf()
    return h * res


def simpson(func, iter_lst, h):
    res = iter_lst[0]
    for i in range(1, len(iter_lst) // 2 + 1):
        res += 4 * func.subs(x, iter_lst[2 * i - 1]).evalf()
    for i in range(1, len(iter_lst) // 2):
        res += 2 * func.subs(x, iter_lst[2 * i]).evalf()
    res += iter_lst[-1]
    return (res * h) / 3


if __name__ == '__main__':
    func = 1 / (sympy.sqrt(x) * (1 - x) ** (3 / 4))
    a = 0
    b = 0.95
    print('Func is ')
    sympy.pprint(func)
    print()
    plot(func, (x, a, b), show=True)
    n = 21  # Count of iter
    h = (b - a) / n

    lst = [a + h * i for i in range(n + 1)]

    print(len(lst))
    # print(lst)
    # f1  = func
    f1 = func.series(x, 0, 8).removeO()
    print(f1)
    f2 = func.series(x, 0, 4).removeO()
    print(f2)
    f1 = f1 - f2
    print(f1)
    inter1 = midl_sq(f1, lst, h)
    inter2 = midl_sq(f2, lst, h)
    print(inter1 + inter2)
    y = sympy.Symbol('y')
    absolut = sympy.integrate(func, (x, y, b))
    print(absolut)

    #
    # integr = midl_sq(func, lst, h)
    # print(integr)
    # absolut = sympy.integrate(func, (x, a, b)).evalf()
    # print(absolut)
    # # print(abs(absolut - integr))
    # simp = simpson(func, lst, h)
    # print(simp)
    # print(f'Средние прямоугольники разнциа {abs(absolut - integr)}')
    # print(f'Симпсон разнциа {abs(simp - absolut)}')
