import sympy as sp

X = sp.Symbol('x')


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

    sigma = sp.expand(sigma)
    print('P(x) = ', sigma)
    ans = sigma.subs(X, 1)
    print(f'f(1) = {ans} = {round(ans, 4)}')


# a)
x = [0, 2, 4, 5]
y = [3, 4, 7, 59]
print('for part a:')
interpolation(x, y)

# b)
x.append(8)
y.append(84)
print('\nfor part b:')
interpolation(x, y)
