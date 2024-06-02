from sympy import *


class systemOfNonlinearEquations():
    def __init__(self, max_iter, e_threshold):
        self.e_s = e_threshold
        self.iterations = max_iter
        self.X, self.F, self.J = [], [], []

        self.variables = input(
            "Please enter the variables separated by a comma and a space (x, y, z, ...): ").split(', ')
        for var in self.variables:
            exec(f"{var} = Symbol('{var}')")

        self.equations = input(
            "Please enter the equations separated by a comma and a space (f, g, h, ...): ").split(', ')
        for eq in self.equations:
            self.F.append([eval(eq)])
        self.F = Matrix(self.F)

        print("Please enter the initial points one by one: ")
        for var in self.variables:
            zero = input(f"{var}0 = ")
            self.X.append([float(zero)])

        self.len = len(self.variables)
        self.JacobianInverse()
        self.NewtonRaphson()

    def JacobianInverse(self):
        for eq in self.equations:
            row = []
            for var in self.variables:
                col = diff(eq, var)
                row.append(col)
            self.J.append(row)

        jacobian = Matrix(self.J)
        self.J_inv = jacobian.inv()

    def NewtonRaphson(self):
        for i in range(1, self.iterations+1):
            X_old = Matrix(self.X)
            substitutes = {var: value for var,
                           value in zip(self.variables, X_old)}
            J_inv = self.J_inv.subs(substitutes).evalf()
            F = self.F.subs(substitutes).evalf()
            X = X_old - J_inv @ F
            e_absolute = abs(X - X_old)
            self.X = X
            print(f"----- iter:{i}\t max(e_abs):{max(e_absolute):.3} -----")
            self.result()

            if max(e_absolute) <= self.e_s:
                print(f"The answer is found in {i}th iteration as:")
                self.result()
                return X

    def result(self):
        for var, val in zip(self.variables, self.X):
            print(var, "=", val.evalf(6))
        print()


test = systemOfNonlinearEquations(1000, 10**-5)
'''
Best examples:
    y+x**2-x-0.75
    y+5*x*y-x**2
    x0 = y0 = 1.2
    The answer is found in 5th iteration as:
    x = 1.37207
    y = 0.239502

    x**2 + y**2 - 25
    y**2 - x - 5
    x0=3, y0=4
    The answer is found in 3th iteration as:
    x = 4.00000
    y = 3.00000
'''
