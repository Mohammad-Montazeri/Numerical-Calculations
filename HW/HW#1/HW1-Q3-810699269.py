import sympy as sp

# defining the variables and function r:
x, y, z = sp.symbols('x,y,z')
r = sp.sqrt(x ** 2 + y ** 2 + z ** 2)
e = sp.Symbol('e')
ex = ey = ez = e

# defining the error of the function using its formula:
err = ex * abs(sp.diff(r, x)) + ey * abs(sp.diff(r, y)) + ez * abs(sp.diff(r, z))

# substituting values for x & y & z:
err = err.subs([(x, 1), (y, 2), (z, 3)])

# solving the uniqualty error < 1 :
a = sp.solveset(err < 1, e, sp.S.Reals)
print(a)
print(f'maximum value of e would be {a.right} = {(a.right).evalf()}')
