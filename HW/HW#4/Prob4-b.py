from sympy import *


# problem 4, part b)

# err of Simpson method is (b-a)/180 * h^4 * f""

a, b = 0, 1
x = Symbol('x')
f = 1 / (x ** 2 + 1)
f_p = diff(f, x)
f_pp = diff(f_p, x)
f_3 = diff(f_pp, x)
f_4 = diff(f_3, x)
print(f'f""(x) = {f_4}')
plot(f_4, (x, -1, 1))

max_f4 = maximum(f_4, x, Interval(0, 1))
print(f'maximum value of f"" in [0,1] is {max_f4}')
# according to the plot shown, f""(x) reaches its maximum at x = 0 in [0,1];
# and as f""(0) = 24 , the result calculated atop is as expected.
# from now on, we use term <err> for maiximum error of Simpson's method.


n = 0
err = 1
while err >= 0.5 * 10 ** (-4):
    n += 1
    h = (b - a) / n
    err = (b - a) / 180 * h ** 4 * max_f4
    print(f'error at stage {n} = {float(err)}')

print(f'at n = {n} \t , \t h = {h} we\'ll satisfy wanted precision;')


def f(x):
    return 1 / (x ** 2 + 1)


points = [a]
t = a
for i in range(n):
    t += h
    points.append(t)

Fard = [points[i] if i % 2 == 1 else 0 for i in range(n + 1)]
Odds = [f(i) if i != 0 else 0 for i in Fard]
odd = sum(Odds)

Zowj = [points[i] if i % 2 == 0 and i not in (0, n) else 0 for i in range(n + 1)]
Evens = [f(i) if i != 0 else 0 for i in Zowj]
even = sum(Evens)

I = (b - a) * (f(a) + f(b) + 4 * odd + 2 * even) / (3 * n)
print(f'so at this stage, final answer for I is {I}')