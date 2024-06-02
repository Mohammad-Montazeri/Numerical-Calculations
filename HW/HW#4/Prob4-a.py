from sympy import *

# problem 4, part a)

# err of Trapezius method is (b-a)/12 * h^2 * f"

a, b = 0, 1
x = Symbol('x')
f = 1 / (x ** 2 + 1)
f_p = diff(f, x)
f_pp = diff(f_p, x)
print(f'f"(x) = {f_pp}')
plot(f_pp, (x, -3, 3))

max_fpp = maximum(f_pp, x, Interval(0, 1))
print(f'maximum value of f" in [0,1] is {max_fpp}')
# according to the plot shown,
# f"(x) is ascendant in [0,1];
# so it's expected that maximum value of f" be reached at x = 1.
# and as f"(1) = 0.5 , the result calculated atop is as expected.
# from now on, we use term <err> for maiximum error of Trapezius method.


n = 0
err = 1
while err >= 0.003:
    n += 1
    h = (b - a) / n
    err = (b - a) / 12 * h ** 2 * max_fpp
    print(f'error at stage {n} = {float(err)}')

print(f'n = {n} \t and \t h = {h}')





# another vision to solve this problem:

# a, b = 0, 1
# x = Symbol('x')
# f = 1 / (x ** 2 + 1)
# true_value = integrate(f, (x, a, b))
# print(f'the true answer of the integral = {true_value}')
# n = 0
# err = 1
# while err >= 0.003:
#     n += 1
#     h = (b - a) / n
#     list = [a]
#     sigma = 0
#     t = a
#     for i in range(n):
#         t += h
#         list.append(t)
#
#     for i in list:
#         if i == a or i == b:
#             sigma += f.subs(x, i)
#         else:
#             sigma += 2 * f.subs(x, i)
#
#     I = (b - a) * sigma / (2 * n)
#     err = abs((true_value - I) / true_value)
#     print(f'error at stage {n}= {float(err)}')
#
#
# print(f'finally, the I is calculated {round(I, 4)} with error {round(err, 4)}.'
#       f'\nn is {n} at this stage so h is equal to {h}.')
