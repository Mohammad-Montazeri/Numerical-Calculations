from sympy import *


# f = lambda x : (x+pi)*cos(2*x)*sin(x)
def f(x):
    return (x + pi) * cos(2 * x) * sin(x)


X = Symbol('x')
x = [0, pi / 4, pi / 3, pi / 2]
y = [f(i) for i in x]


def interpolation(x, y):
    n = len(x)
    sigma = 0
    for i in range(n):

        L = 1
        for j in range(n):
            if i is not j:
                p = (X - x[j]) / (x[i] - x[j])
                L *= p

        sigma += L * y[i]

    return expand(sigma)


P = interpolation(x, y)
print('P(x) = ', P)

a = plot(f(X), (X, 0, pi / 2), label='f(x)', show=False, legend=True)
b = plot(P, (X, 0, pi / 2), label='P(x)', show=False, legend=True)

a.append(b[0])
a.show()
