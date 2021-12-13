import sympy
import matplotlib.pyplot as plt
import numpy as np
from threading import Thread
from math import *
import numba
import random
from sympy.plotting import plot

x = sympy.Symbol('x')


def simple_iteration(a, b, func, eps, iterfunc, q):
    x0 = random.uniform(a, b)
    print(f'Start x0 = {x0}')
    x1 = iterfunc.subs(x, x0)
    iter = 1
    print((((1 - q) / q) * eps))
    while abs(x1 - x0) > (((1 - q) / q) * eps):
        print(x1)
        x0 = x1.evalf()
        x1 = iterfunc.subs(x, x0).evalf()
        iter += 1
    return x1, iter
    # pass


def get_ax_ay(a, b, func, step):
    a = int(a / step)
    b = int(b / step)
    ax = []
    ay = []
    for i in range(a, b):
        ay.append(func.subs(x, i * step))
        ax.append(i * step)
    return ax, ay


if __name__ == '__main__':
    func = 5 * x - 8 * sympy.log(x) - 8
    # iterfunc = (8 * sympy.log(x))/5
    iterfunc = sympy.exp((5 / 8) * x - 1)
    # func  = x ** 2 -2
    print('Func is ')
    sympy.pprint(func)
    print('')
    eps = 0.0001
    # print(get_ax_ay(0, 10, func, 0.01))
    #
    graph = plot(func, (x, -4, 4), show=False)
    graph.show()
    graph = plot(abs(iterfunc.diff(x)), (x, 0, 5), show=True)

    ax, ay = get_ax_ay(0.1, 4, func, 0.001)
    plt.title("Our func graph")  # заголовок
    plt.xlabel("x")  # ось абсцисс
    plt.ylabel("y")  # ось ординат
    plt.grid()  # включение отображение сетки
    plt.plot(ax, ay, "r")  # построение графика

    solution = sympy.solve(func, x)

    for i in solution:
        print(i.evalf())
    # print(sympy.evalf(solution))

    solution, iter = simple_iteration(0, 1, func, eps, iterfunc, 0.55)
    plt.plot([solution], [func.subs(x, solution)], 'k*')
    #
    # print(solution)
    #
    plt.show()
    print(solution, iter)
