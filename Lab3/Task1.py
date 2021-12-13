import sympy
import matplotlib.pyplot as plt
import numpy as np
from threading import Thread
from math import *
from sympy.plotting import plot
x = sympy.Symbol('x')


# @numba.njit()
def dihotomia(a, b, func, eps):
    mid = (b + a) / 2
    iter = 0
    if a > b:
        raise ValueError

    while (abs(b-a)) >= 2 * eps:
        iter += 1
        mid = (b + a) / 2
        # if abs( func.subs(x, mid) - func.subs(x, a)) < eps:
        #     tmp = 0
        # else:
        tmp = func.subs(x, mid) * func.subs(x, a)
        # print(tmp, ' -- ', mid)
        if tmp < 0:
            b = mid
        elif tmp > 0:
            a = mid
        else:
            # print(a , b )
            return mid, iter
    return mid, iter
            # a = b
        # ITERATIONS +=1


# @numba.njit()
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
    func = sympy.exp(-x) - x ** 2
    # func  = x ** 2 -2
    print('Func is ')
    sympy.pprint(func)
    eps = 0.0001
    # print(get_ax_ay(0, 10, func, 0.01))
    graph = plot(func, (x, 0, 2), show=False)
    graph.show()

    lfunc = sympy.exp(-x)
    # lfunc = 2  + 0*x
    rfunc = x ** 2
    ax, ay = get_ax_ay(0, 2, func, 0.001)
    plt.title("Our func graph")  # заголовок
    plt.xlabel("x")  # ось абсцисс
    plt.ylabel("y")  # ось ординат
    plt.grid()  # включение отображение сетки
    plt.plot(ax, ay, "r")  # построение графика
    # ax, ay = get_ax_ay(0, 2, rfunc, 0.001)
    # plt.plot(ax, ay, "b")  # построение графика
    solution = sympy.solve(func, x)

    for  i in solution:
        print(i.evalf())
    # print(sympy.evalf(solution))

    solution, iter = dihotomia(0.5, 0.8, func, eps)
    plt.plot([solution], [func.subs(x, solution)], 'k*')

    print(solution)
    plt.plot([solution] , [func.subs(x , solution)] , 'g*')

    plt.show()
    print(solution, iter)
