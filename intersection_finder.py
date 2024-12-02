from sympy import symbols, diff, sympify


#App Header/Start Menu

program_header = """

> Welcome to The Functions Intersection Point Finder


> Program capabilities:
        $ The program only supports 2 functions
        $ Only polynomial functions are supported

> Instructions:
        $ To enter a function, write the function in lower-case
        $ Symboles allowed:
            # Addition: +
            # Subtraction: -
            # Multiplication: *
            # Division: /
            # Exponentiation (power): **
                 """

print(program_header)

input_f = input("Function 1: ").lower
input_g = input("Function 2: ").lower

x,y,z = symbols("x y z") # define variables

f = sympify(input_f) # function 1
g = sympify(input_g) # function 2

F = [[f],            # F-matrix (original functions matrix)
     [g]]

J = [[diff(f,x),diff(f,y),diff(f,z)],
     [diff(g,x),diff(g,y),diff(g,z)]]

point : int = [[1],  # guess point (x,y) = (1,1)
               [1]]

