from numpy import *

F = lambda x, y: array([[log(x ** 2 + y ** 2) + y - 1],
                        [sqrt(x) + x * y]])

j = lambda x, y: array([[2 * x / (x ** 2 + y ** 2), 2 * y / (x ** 2 + y ** 2) + 1],
                        [y + 1 / (2 * sqrt(x)), x]])

J_inv = lambda x, y: linalg.inv(j(x, y))

x = 2.4
y = -0.6
X = array([[x],
           [y]])

n = int(input('please enter n = '))
for i in range(n):
    x_new = X - J_inv(x, y) @ F(x, y)

    X = x_new
    x, y = X[0, 0], X[1, 0]

    print(X, '\n')

print(f'the answer for x and y is respectively {round(x, 5)} and {round(y, 5)} with {n} iterations')
