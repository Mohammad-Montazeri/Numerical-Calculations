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
        Secant(lambda s: expression.subs(x, s).evalf())

    except Exception as e:
        print("Error evaluating the expression:", e)


def Secant(f):
    '''
    Best example: f(x) = (x-3)**2 * sin(ln(x))
    roots:  method = 0 (ordinary),   x0, x1 = 2.5, 2.8  ->  xr = 2.9999638 (18 iter)
    roots:  method = 1 (modified),   x1 = 2.5           ->  xr = 3.0005437 (22 iter)

    '''

    # Defining the initial parameters of the problem
    method = int(input("Enter 0 for choosing Secant method or 1 for Modified Secant method: "))
    if method:
        x0, x1 = 0, float(input('Please enter the initial point of x: '))
        delta = 10**-2
    else:
        x0, x1 = eval(
        input('Please enter the initial points of x as a tuple (x0, x1): '))

    e_threshold = 10**-5

    # Implementing the Secant method
    for i in range(1, 1000):

        # Updating the new root and calculating its relative error
        if method:
            x2 = x1 - delta*f(x1) / (f(x1 + delta) - f(x1))
        else:
            x2 = x1 - (f(x1) * (x0 - x1)) / (f(x0) - f(x1))
        e_relative = abs((x2 - x1)/x2)

        if f(x2) == 0 or e_relative < e_threshold:
            print(
                f'The root is found as{style.B} x = {x2} {style.E}in the {i}th iteration.')
            return True

        # Updating the old roots
        x0, x1 = x1, x2

    print(
        f'The closest x to an actual root, found with 1000 iterations: x = {x2}')


main()
