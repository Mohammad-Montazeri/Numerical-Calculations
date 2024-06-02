from numpy import pi

Q = 4 * 10 ** 5
q = 2 * 10 ** 5
r = 0.2
epsilon = 8.9 * 10 ** 9


def f(x):
    F = q * Q * x / (4 * pi * epsilon * (x ** 2 + r ** 2) ** 1.5)
    return F - 2


x = [0.75, 1]       # [x0 , x1]
for i in range(2, 30):

    x_new = x[i - 1] - f(x[i - 1]) * (x[i - 2] - x[i - 1]) / (f(x[i - 2]) - f(x[i - 1]))
    x.append(x_new)
    if f(x_new) == 0:
        break

print(f'the answer for x is {x_new} m')
