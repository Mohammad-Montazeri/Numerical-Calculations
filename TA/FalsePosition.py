from sympy import *

# Define the variable
x = symbols('x')

# Defining a text style class to highlight the results
class style:
    B = '\033[1;34m'    # Bold and Blue
    E = '\033[0m'       # Back to default


def main():
    # Get expression from the user
    expression_str = input(
        "Please enter the function whose roots you want to find, as a function of x: ")

    try:
        # Evaluate the expression
        expression = eval(expression_str)

        # Print the result
        print(f"Expression accepted as:{style.B}", expression, style.E)

        # Evaluating and passing the expression as a function of x
        FalsePosition(lambda s: expression.subs(x, s))

    except Exception as e:
        print("Error evaluating the expression:", e)


def FalsePosition(f):
    bounds = eval(
        input('Please enter the initial points of x as a tuple (xl, xu): '))
    xl, xu = bounds
    if f(xl) * f(xu) > 0:
        raise ValueError('There is no root between these points')

    e_threshold = 10**-5
    il = iu = xm = 0
    fu, fl = f(xu).evalf(), f(xl).evalf()
    for i in range(1, 1000):
        xr = xm
        xm = xu - (fu * (xl - xu)) / (fl - fu)
        e_relative = abs((xm - xr)/xm)
        if f(xm) == 0 or e_relative < e_threshold:
            print(
                f'The root is found as{style.B} x = {xm} {style.E}in the {i}th iteration.')
            return True
        elif f(xl)*f(xm) >= 0:
            xl = xm
            fl = f(xl).evalf()
            il = 0
            iu += 1
            if iu > 3:
                fu /= 2
                iu = 0
        else:
            xu = xm
            fu = f(xu).evalf()
            iu = 0
            il += 1
            if il > 3:
                fl /= 2
                il = 0
    print(
        f'The closest x to an actual root, found with 1000 iterations: x = {xm}')


main()
