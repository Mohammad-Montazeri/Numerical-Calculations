from numpy import *
import matplotlib.pyplot as plt
import math

a = float(input('enter a number for a as the lower bound of [a,b]:\t'))
b = float(input('enter a number for b as the upper bound of [a,b]:\t'))
n = int(input('enter a number for n as the number of repetitions:\t'))


def f(x):
    return tan(x) + tanh(x)


if f(a) * f(b) > 0 or a > b:
    print(f'there is no root in this range [{a},{b}]')

elif math.ceil(b / pi + 0.5) - math.floor(a / pi + 0.5) > 1:
    print(f'there is some discontinuity for f(x) in this range [{a},{b}]')

else:

    for i in range(n):
        x = (a + b) / 2
        if f(x) * f(a) == 0:
            break
        elif f(x) * f(a) < 0:
            b = x
        else:
            a = x

    print(f'x={x} is the root of the f(x)')

x = linspace(-8,8,1000)
y = f(x)
plt.plot(x,y)
plt.ylim(-8,8)
plt.show()