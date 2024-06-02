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
        "Please enter the function g(x) from the equation x-g(x)=0  ->  x = g(x): ")

    try:
        # Evaluate the expression
        expression = eval(expression_str)

        # Print the result
        print(f"Expression accepted as:{style.B}", expression, style.E)

        # Evaluating and passing the expression as a function of x
        FixedPoint(lambda s: expression.subs(x, s))

    except Exception as e:
        print("Error evaluating the expression:", e)


def FixedPoint(g):
    # Get the initial value of method and check convergence criterion
    x0 = eval(input('Please enter the initial guess: '))
    criterion = abs(diff(g(x)).subs(x, x0).evalf())
    if criterion <= 1:
        print('|g\'(x0)| =', criterion)
    else:
        raise ValueError(
            'The chosen g(x) causes divergence for fixed point iteration method: |g\'(x0)| > 1')

    # Initialize loop parameters
    xr = x0
    e_threshold = 10**-5

    # Implement the fixed point iteration method with maximum of 1000 iterations
    for i in range(1, 1000):

        # Update the hypothetical root value
        x_old = xr
        xr = g(x_old).evalf()

        # Calculate the relative error
        e_relative = abs((xr - x_old)/xr)

        print(f'iter:{i}\t\t xr:{xr:.4f}\t e_a:{e_relative:.4f}')

        # Check if the already found answer meets the desired precision
        if g(xr) == 0 or e_relative < e_threshold:
            print(
                f'The root is found as{style.B} x = {xr} {style.E}in the {i}th iteration.')
            return True
    print(
        f'The closest x to an actual root, found with 1000 iterations: x = {xr}')


main()
