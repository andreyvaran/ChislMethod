import sympy as sp
import math

from typing import *

x = sp.Symbol('x')
y = sp.Symbol('y')
z = sp.Symbol('z')
t = sp.Symbol('t')
u = sp.Symbol('u')
# Коофициенты для метода рунге
p1, p2, p3 = 1, (1 / 6), (-1 / 6)
a2, a3 = -7 / 6, 11 / 6
b32, b21, b31 = -6 / 7, -7 / 6, 113 / 42


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




def make_all(n):
    a = 0
    b = 2
    h = (b- a)/n



if __name__ == '__main__':
    print(type(...))


