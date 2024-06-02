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
        Bisection(lambda s: expression.subs(x, s))

    except Exception as e:
        print("Error evaluating the expression:", e)


def Bisection(eq):
    bounds = eval(
        input('Please enter the initial points of x as a tuple (xl, xu): '))
    xl, xu = bounds
    if eq(xl) * eq(xu) > 0:
        raise ValueError('There is no root between these points')

    e_threshold = 10**-5
    for i in range(1, 1000):
        xm = (xl+xu)/2
        e_relative = abs((xu - xl) / (xu + xl))
        if eq(xm) == 0:
            print(
                f'The exact root is found as{style.B} x = {xm} {style.E}in the {i}th iteration.')
            return True
        elif e_relative < e_threshold:
            print(
                f'The approximate root is found as{style.B} x = {xm} {style.E}in the {i}th iteration.')
            return True
        elif eq(xl)*eq(xm) >= 0:
            xl = xm
        else:
            xu = xm
    print(
        f'The closest x to an actual root, found with 1000 iterations:{style.B} x = {xm}', style.E)


main()
