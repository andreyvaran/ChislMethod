import sympy
import matplotlib.pyplot as plt
import numpy as np
from threading import Thread
from math import *
import numba
from sympy.plotting import plot

x = sympy.Symbol('x')


def hords(a, b, func, eps):
    x0, x1 = a, b
    iter = 0
    fx = func.subs(x, x1)
    x2 = (x1 - (fx * (x1 - x0)) / (fx - func.subs(x, x0)))
    # print(x2.evalf())
    # print(type(x2))
    # print(func.subs(x, x2).evalf())
    while abs(func.subs(x, x2)) > eps:
        f2 = func.subs(x, x2)
        f0 = func.subs(x, x0)
        iter += 1
        if f2 * f0 < 0:
            x1 = x2
        else:
            x0 = x2
        f1 = func.subs(x, x1)
        x2 = (x1 - (f1 * (x1 - x0)) / (f1 - func.subs(x, x0))).evalf()
        # print(123)
    return x2, iter


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
    func = x ** 2 - 6 - sympy.cos(x ** 2)
    # func  = x ** 2 -2
    print('Func is ')
    sympy.pprint(func)
    eps = 0.0001
    # print(get_ax_ay(0, 10, func, 0.01))
    #
    # graph = plot(func ,(x , -4 , 4),show=False )
    # graph.show()

    ax, ay = get_ax_ay(-0, 4, func, 0.001)
    plt.title("Our func graph")  # заголовок
    plt.xlabel("x")  # ось абсцисс
    plt.ylabel("y")  # ось ординат
    plt.grid()  # включение отображение сетки
    plt.plot(ax, ay, "r")  # построение графика

    # solution = sympy.solve(func, x)
    #
    # for  i in solution:
    #     print(i.evalf())
    # print(sympy.evalf(solution))

    print(f'Solution is  {2.61646} , {-2.61646}')

    solution, iter = hords(2, 3, func, eps)
    plt.plot([solution], [func.subs(x, solution)], 'k*')

    print(solution)

    plt.show()
    print(solution, iter)
