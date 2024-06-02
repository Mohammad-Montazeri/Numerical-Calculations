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

        # Passing the function to the solver method
        NewtonRaphson(expression)

    except Exception as e:
        print("Error evaluating the expression:", e)


def NewtonRaphson(function):
    '''
    Best example: f(x) = (x-3)**2 * sin(ln(x)) which has many roots with small to big gaps between
    roots:  m = 1  x1 = 0.002   ->  xr = 0.001867
    roots:  m = 1  x1 = 0.02    ->  xr = 0.043213
    roots:  m = 1  x1 = 0.2     ->  xr = 2.999982
    roots:  m = 1  x1 = 0.8     ->  xr = 1.000000
    roots:  m = 1  x1 = 0.8     ->  xr = 1.000000
    roots:  m = 1  x1 = 2.5     ->  xr = 2.999973   (14 iterations)
    roots:  m = 2  x1 = 2.5     ->  xr = 3.000000   (04 iterations)
    roots:  m = 0  x1 = 2.5     ->  xr = 3.000000   (04 iterations)
    '''

    # Evaluating the expression and its derivative(s) as functions of x
    def f(s): return function.subs(x, s).evalf()
    def fp(s): return function.diff(x).subs(x, s).evalf()

    m = int(input("Enter the degree of multiplicity of roots for this problem. \nEnter 0 if it's more than 2 but you're not sure how much: "))
    if not m:
        def fpp(s): return function.diff(x).diff(x).subs(x, s).evalf()

    # Get the initial value of method and check convergence criterion
    x0 = eval(input('Please enter the initial guess: '))

    # Initialize loop parameters
    xr = x0
    e_threshold = 10**-5

    # Implement the Newton Raphson method with a maximum of 1000 iterations
    for i in range(1, 1000):

        # Update the hypothetical root value
        x_old = xr
        if m:
            xr = x_old - m*f(x_old)/fp(x_old)
        else:
            xr = x_old - (f(x_old)*fp(x_old)) / (fp(x_old)**2 - f(x_old)*fpp(x_old))

        # Calculate the relative error
        e_relative = abs((xr - x_old)/xr)

        print(f'iter:{i}\t\t xr:{xr:.4f}\t e_a:{e_relative:.4f}')

        # Check if the already found answer meets the desired precision
        if f(xr) == 0 or e_relative < e_threshold:
            print(
                f'The root is found as{style.B} x = {xr} {style.E}in the {i}th iteration.')
            return True
    print(
        f'The closest x to an actual root, found with 1000 iterations: x = {xr}')


main()
