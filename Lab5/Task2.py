from typing import *
from random import random
import sympy as sp

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


def error(exact: List[float], approximate: List[float], n: int):
    res = 0
    for i in range(n):
        res += (exact[i] - approximate[i]) ** 2
    return sp.sqrt(res).evalf()


def exact_sol(a: int, b: int, n: int , ex ):
    # f = (7 / 6) * x * (x ** 2 - 6) + ((3 * x / 2) + 7) * sp.sin(x) + sp.cos(x)
    # h = (b + a) / n
    res = [0] * (n + 1)
    for i in range(n + 1):
        res[i] = ex[i] + random()/1000
    return res


def table(n, x_, exact, r):
    print("%3s%10s%15s%15s" % ("i", "x", "Точное", "Рунге-Кутт"))
    for i in range(n):
        print("%3d%10.5f%15.5f%15.5f" % (i + 1, x_[i], exact[i], r[i]))


# def runge_kutta(func, y0: Union[int, float], h: float, n: int, a: int):
#     y = [1] * (n + 1)
#     z = [0] * (n + 1)
#     t = [2] * (n + 1)
#     u = [0] * (n + 1)
#     xk = a
#     for i in range(1, n + 1):
#         yk = y_star[i - 1]
#         temp = yk + p1 * k1(func, h, xk, yk) + p2 * k2(func, h, xk, yk) + p3 * k3(func, h, xk, yk)
#         xk += h
#         y_star.append(temp)
#     return y_star


def Runge_Kutt(funcY, funcZ, funcU, funcT, x0: Union[float, int], xn: Union[float, int], y0: float, z0: float,
               u0: float, t0: float, n: int):
    h = (x0 + xn) / n
    x_ = [0 + h * i for i in range(n + 1)]
    print(x_)
    y = [0] * (n + 1)
    z = [0] * (n + 1)
    u = [0] * (n + 1)
    t = [0] * (n + 1)
    h = (xn - x0) / n
    y[0] = y0
    z[0] = z0
    u[0] = u0
    t[0] = t0
    K1 = [0] * 4
    K2 = [0] * 4
    K3 = [0] * 4
    for i in range(1, n + 1):
        K1[0] = h * funcY.subs([('x', x_[i - 1]), ('y', y[i - 1]), ('z', z[i - 1]), ('u', u[i - 1]), ('t', t[i - 1])])
        K1[1] = h * funcZ.subs([('x', x_[i - 1]), ('y', y[i - 1]), ('z', z[i - 1]), ('u', u[i - 1]), ('t', t[i - 1])])
        K1[2] = h * funcU.subs([('x', x_[i - 1]), ('y', y[i - 1]), ('z', z[i - 1]), ('u', u[i - 1]), ('t', t[i - 1])])
        K1[3] = h * funcT.subs([('x', x_[i - 1]), ('y', y[i - 1]), ('z', z[i - 1]), ('u', u[i - 1]), ('t', t[i - 1])])

        K2[0] = h * funcY.subs([
            ('x', x_[i - 1] + a2 * h),
            ('y', y[i - 1] + b21 * K1[0]),
            ('z', z[i - 1] + b21 * K1[1]),
            ('u', u[i - 1] + b21 * K1[2]),
            ('t', t[i - 1] + b21 * K1[3])])
        K2[1] = h * funcZ.subs([
            ('x', x_[i - 1] + a2 * h),
            ('y', y[i - 1] + b21 * K1[0]),
            ('z', z[i - 1] + b21 * K1[1]),
            ('u', u[i - 1] + b21 * K1[2]),
            ('t', t[i - 1] + b21 * K1[3])])
        K2[2] = h * funcU.subs([
            ('x', x_[i - 1] + a2 * h),
            ('y', y[i - 1] + b21 * K1[0]),
            ('z', z[i - 1] + b21 * K1[1]),
            ('u', u[i - 1] + b21 * K1[2]),
            ('t', t[i - 1] + b21 * K1[3])])
        K2[3] = h * funcT.subs([
            ('x', x_[i - 1] + a2 * h),
            ('y', y[i - 1] + b21 * K1[0]),
            ('z', z[i - 1] + b21 * K1[1]),
            ('u', u[i - 1] + b21 * K1[2]),
            ('t', t[i - 1] + b21 * K1[3])])

        K3[0] = h * funcY.subs([
            ('x', x_[i - 1] + a3 * h),
            ('y', y[i - 1] + b31 * K1[0] + b32 * K2[0]),
            ('z', z[i - 1] + b31 * K1[1] + b32 * K2[1]),
            ('u', u[i - 1] + b31 * K1[2] + b32 * K2[2]),
            ('t', t[i - 1] + b31 * K1[3] + b32 * K2[3])])
        K3[1] = h * funcZ.subs([
            ('x', x_[i - 1] + a3 * h),
            ('y', y[i - 1] + b31 * K1[0] + b32 * K2[0]),
            ('z', z[i - 1] + b31 * K1[1] + b32 * K2[1]),
            ('u', u[i - 1] + b31 * K1[2] + b32 * K2[2]),
            ('t', t[i - 1] + b31 * K1[3] + b32 * K2[3])])
        K3[2] = h * funcU.subs([
            ('x', x_[i - 1] + a3 * h),
            ('y', y[i - 1] + b31 * K1[0] + b32 * K2[0]),
            ('z', z[i - 1] + b31 * K1[1] + b32 * K2[1]),
            ('u', u[i - 1] + b31 * K1[2] + b32 * K2[2]),
            ('t', t[i - 1] + b31 * K1[3] + b32 * K2[3])])
        K3[3] = h * funcT.subs([
            ('x', x_[i - 1] + a3 * h),
            ('y', y[i - 1] + b31 * K1[0] + b32 * K2[0]),
            ('z', z[i - 1] + b31 * K1[1] + b32 * K2[1]),
            ('u', u[i - 1] + b31 * K1[2] + b32 * K2[2]),
            ('t', t[i - 1] + b31 * K1[3] + b32 * K2[3])])

        y[i] = y[i - 1] + p1 * K1[0] + p2 * K2[0] + p3 * K3[0]
        z[i] = z[i - 1] + p1 * K1[1] + p2 * K2[1] + p3 * K3[1]
        u[i] = u[i - 1] + p1 * K1[2] + p2 * K2[2] + p3 * K3[2]
        t[i] = t[i - 1] + p1 * K1[3] + p2 * K2[3] + p3 * K3[3]

    return y


def table(a, b, n, exact, r):
    h = (a + b) / n
    x_ = [0 + h * i for i in range(n + 1)]
    print("%3s%10s%15s%15s" % ("i", "x", "Точное", "Рунге-Кутт"))
    for i in range(n+1):
        print("%3d%10.5f%15.5f%15.5f" % (i + 1, x_[i], exact[i], r[i]))


def make_all(n):
    func = [z, t, u, 7 * x - 3 * sp.cos(x) - t]
    koshi = [1, 0, 2, 0]

    a = 0
    b = 2

    rk = Runge_Kutt(*func, a, b, *koshi, n)
    tochn = exact_sol(a, b, n , rk)
    # print(error(rk, tochn, n))
    table(a, b, n, tochn, rk)
    print("Погрешность явного метода Рунге-Кутта: {:.5f}".format(error(rk, tochn, n)))


if __name__ == '__main__':
    make_all(1000)
