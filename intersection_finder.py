from sympy import symbols, diff, sympify,lambdify,Matrix
import matplotlib.pyplot as plt
import numpy as np
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

input_f = input("Function 1: ")
input_g = input("Function 2: ")

x,y,z = symbols("x y z")  # define variables

f = sympify(str(input_f)) # function 1
g = sympify(str(input_g)) # function 2

F = Matrix([[f],          # F-matrix (original functions matrix)
            [g]])

J = Matrix([[diff(f,x),diff(f,y)],
            [diff(g,x),diff(g,y)]])


if J.det() == 0:
    print("Jacobian is singular at the point.")
    exit()

point = np.array([1,1])
tolerance = 1e-3

f_numeric = lambdify((x, y), f, 'numpy')
g_numeric = lambdify((x, y), g, 'numpy')
f_prime_x = lambdify((x, y), diff(f, x), 'numpy')
f_prime_y = lambdify((x, y), diff(f, y), 'numpy')
g_prime_x = lambdify((x, y), diff(g, x), 'numpy')
g_prime_y = lambdify((x, y), diff(g, y), 'numpy')


while True:
    J = np.array([[f_prime_x(point[0], point[1]), f_prime_y(point[0], point[1])],
                  [g_prime_x(point[0], point[1]), g_prime_y(point[0], point[1])]])
    
   
    F_val = np.array([f_numeric(point[0], point[1]), g_numeric(point[0], point[1])])

    J_inv = np.linalg.inv(J)
    
    new_point = point - np.dot(J_inv, F_val)

    # Check for convergence
    if np.linalg.norm(F_val) < tolerance or np.linalg.norm(new_point - point) < tolerance:
        break
    else:
        point = new_point
        

intersection_point = (round(((point[0])).item()), round((point[1]).item()))

print(f"computed intersection point is {intersection_point}")

