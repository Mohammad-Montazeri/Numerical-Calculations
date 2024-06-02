from sympy import *

# problem 4, part c)

a, b = 0, 1
t = Symbol('t')

X = (b - a) / 2 * t + (b + a) / 2
c = (b - a) / 2

F_x = 1 / (X ** 2 + 1)

def f_t(s):
    return F_x.subs(t, s)

# 3 point Gauss argument:
arg = sqrt(3 / 5)

I = c * (1 / 9 * (5 * f_t(-arg) + 8 * f_t(0) + 5 * f_t(arg)))
print(f'I is predicted as {I} by 3-point-Gauss method.')