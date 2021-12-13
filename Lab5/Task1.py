import math
from typing import *

from sympy import *

# Var 4
x = Symbol('x')
y = Symbol('y')
# Коофициенты для метода рунге
p1, p2, p3 = 1, (1 / 6), (-1 / 6)
a2, a3 = -7 / 6, 11 / 6
b32, b21, b31 = -6 / 7, -7 / 6, 113 / 42


def explicit_euler(func, y0: Union[int, float], h: float, n: int, a):
    y_star = [y0]
    xk = a
    for i in range(1, n + 1):
        temp = y_star[i - 1] + h * (func.subs([(x, xk), (y, y_star[i - 1])]))
        xk += h
        y_star.append(temp)
    return y_star


def implicit_euler(func, y0: Union[int, float], h: float, n: int, a):
    y_star = [y0]
    xk = a
    for i in range(1, n + 1):
        y_temp = y_star[i - 1] + h * (func.subs([(x, xk), (y, y_star[i - 1])]))
        xk += h
        temp = y_star[i - 1] + h * (func.subs([(x, xk), (y, y_temp)]))
        y_star.append(temp)
    return y_star


def hoin(func, y0: Union[int, float], h: float, n: int, a):
    y_star = [y0]
    xk = a
    for i in range(1, n + 1):
        y_temp = y_star[i - 1] + h * (func.subs([(x, xk), (y, y_star[i - 1])]))
        xk += h
        temp = y_star[i - 1] + (h / 2) * (
                func.subs([(x, xk), (y, y_star[i - 1])]) + func.subs([(x, xk + h), (y, y_temp)]))
        y_star.append(temp)
    return y_star


def k1(func, h: float, xk: float, yk: float):
    return h * func.subs([(x, xk), (y, yk)])


def k2(func, h: float, xk: float, yk: float):
    yk += b21 * k1(func, h, xk, yk)
    xk += a2 * h
    return h * func.subs([(x, xk), (y, yk)])


def k3(func, h: float, xk: float, yk: float):
    yk += b31 * k1(func, h, xk, yk) + b32 * k2(func, h, xk, yk)
    xk += a3 * h
    return h * func.subs([(x, xk), (y, yk)])


def runge_kutta(func, y0: Union[int, float], h: float, n: int, a: int):
    y_star = [y0]
    xk = a
    for i in range(1, n + 1):
        yk = y_star[i - 1]
        temp = yk + p1 * k1(func, h, xk, yk) + p2 * k2(func, h, xk, yk) + p3 * k3(func, h, xk, yk)
        xk += h
        y_star.append(temp)
    return y_star


def correct_list(func, h: float, a, n):
    y_corr = []
    xk = a
    for i in range(n + 1):
        y_corr.append(func.subs(x, xk).evalf())
        xk += h
    return y_corr


def delt(exact: List[float], received: List[float]):
    res = 0
    for i in range(n + 1):
        temp = abs(exact[i] - received[i]) ** 2
        res += temp
    return math.sqrt(res)


def make_all(n):
    a = 1
    b = 1.5
    y0 = 0
    h = abs(a - b) / n

    print("{:^3}".format('i'),
          "{:^5}".format("x[i]"),
          "{:^18}".format("Точное"),
          "{:^18}".format("Явн м.Эйлера"),
          "{:^18}".format("Не явн м.Эйлера"),
          "{:^18}".format("Хойна"),
          "{:^18}".format("Рунге-Кутта"),
          sep='|', end='|\n')
    ex_el = list(map(float, explicit_euler(f, y0, h, n, a)))
    im_el = list(map(float, implicit_euler(f, y0, h, n, a)))
    hoink = list(map(float, hoin(f, y0, h, n, a)))
    runge = list(map(float, runge_kutta(f, y0, h, n, a)))
    correct = list(map(float, correct_list(res, h, a, n)))
    xn = a
    # print(ex_el)
    # print(im_el)
    # print(hoink)
    # print(runge)
    # print(correct)
    for i in range(n + 1):
        print("{:^3d}".format(i),
              "{:^5.3f}".format(xn),
              "{:^18.5f}".format(correct[i]),
              "{:^18.5f}".format(ex_el[i]),
              "{:^18.5f}".format(im_el[i]),
              "{:^18.5f}".format(hoink[i]),
              "{:^18.5f}".format(runge[i]),
              sep='|', end='|\n')
        xn += h
    print('Погрешность явного метода Эйлера : {}'.format(delt(correct, ex_el)))
    print('Погрешность неявного метода Эйлера : {}'.format(delt(correct, im_el)))
    print('Погрешность метода Хойна: : {}'.format(delt(correct, hoink)))
    print('Погрешность метода Рунге-Кутта : {}'.format(delt(correct, runge)))


if __name__ == '__main__':
    f = y / x + (1 / (x ** 2)) + y ** 2

    n = int(input("Enter n "))

    F = Function('F')
    # funct = diff(F(x), x) - F(x) / x - 1 / (x ** 2) - (F(x) ** 2)
    # pprint(funct)
    # res = dsolve(funct , F(x) , ics= {F(a): 1}).rhs   # не получилось посчитать через симпай , пришлось считать через фольфрам
    res = log(x) / (x - x * log(x))
    # pprint(res)
    while (n != 0):
        make_all(n)
        n = int(input('Enter n '))
    print("Прощай любимый пользователь ")
