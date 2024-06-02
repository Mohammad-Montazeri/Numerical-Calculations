# from numpy import *
#
# F = lambda x, y: array([[log(x ** 2 + y ** 2) + y - 1],
#                         [sqrt(x) + x * y]])
#
# j = lambda x, y: array([[2 * x / (x ** 2 + y ** 2), 2 * y / (x ** 2 + y ** 2) + 1],
#                         [y + 1 / (2 * sqrt(x)), x]])
#
# J_inv = linalg.inv(j(x, y))
#
# print(F(1,2))
# print(J_inv(1,2))


a = lambda x, y : x*y

print(a(2,3))

b = 2* a(x,y)

print(b(2,3))
b()