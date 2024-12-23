from sympy import symbols, diff, sympify,lambdify,Matrix
import numpy as np

program_header = """

> Welcome to The Functions Intersection Point Finder


> Program capabilities:
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
dimension = int(input("please enter the number of functions, options: [2,3]:  "))

if dimension == 2:
    user_guess = input("Please enter the initial point in the form of (x,y) and press enter")
    p1,p2 = user_guess.split(",")
    point = np.array([int(p1.strip()),int(p2.strip())])

if dimension == 3:
    user_guess = input("Please enter the initial point in the form of (x,y,z) and press enter")
    p1,p2,p3 = user_guess.split(",")
    point = np.array([int(p1.strip()),int(p2.strip()),int(p3.strip())])
    

input_f = input("Function 1: ")
input_g = input("Function 2: ")

if dimension == 3:
    input_q = input("Function 3: ")

x,y,z = symbols("x y z")  # define variables

f = sympify(str(input_f)) # function 1
g = sympify(str(input_g)) # function 2
if dimension == 3:
    q = sympify(str(input_q))



    

tolerance = 1e-3

if dimension == 2:
    f_numeric = lambdify((x, y), f, 'numpy')
    g_numeric = lambdify((x, y), g, 'numpy')
    
    f_prime_x = lambdify((x, y), diff(f, x), 'numpy')
    f_prime_y = lambdify((x, y), diff(f, y), 'numpy')
   
    g_prime_x = lambdify((x, y), diff(g, x), 'numpy')
    g_prime_y = lambdify((x, y), diff(g, y), 'numpy')

if dimension == 3:
    f_numeric = lambdify((x, y, z), f, 'numpy')
    g_numeric = lambdify((x, y, z), g, 'numpy')
    q_numeric = lambdify((x, y, z), q, 'numpy')
    
    f_prime_x = lambdify((x, y, z), diff(f, x), 'numpy')
    f_prime_y = lambdify((x, y, z), diff(f, y), 'numpy')
    f_prime_z = lambdify((x, y, z), diff(f, z), 'numpy')
   
    g_prime_x = lambdify((x, y, z), diff(g, x), 'numpy')
    g_prime_y = lambdify((x, y, z), diff(g, y), 'numpy')
    g_prime_z = lambdify((x, y, z), diff(g, z), 'numpy')
    
    q_prime_x = lambdify((x, y, z), diff(q, x), 'numpy')
    q_prime_y = lambdify((x, y, z), diff(q, y), 'numpy')
    q_prime_z = lambdify((x, y, z), diff(q, z), 'numpy')


# Initial Jacobian matrix and its inverse
if dimension == 2:
    J = np.array([[f_prime_x(point[0], point[1]), f_prime_y(point[0], point[1])],
                  [g_prime_x(point[0], point[1]), g_prime_y(point[0], point[1])]])
elif dimension == 3:
    J = np.array([[f_prime_x(point[0], point[1], point[2]), f_prime_y(point[0], point[1], point[2]), f_prime_z(point[0], point[1], point[2])],
                  [g_prime_x(point[0], point[1], point[2]), g_prime_y(point[0], point[1], point[2]), g_prime_z(point[0], point[1], point[2])],
                  [q_prime_x(point[0], point[1], point[2]), q_prime_y(point[0], point[1], point[2]), q_prime_z(point[0], point[1], point[2])]])

J_inv = np.linalg.inv(J)

while True:
    if dimension == 2:
        F_val = np.array([f_numeric(point[0], point[1]), g_numeric(point[0], point[1])])
    elif dimension == 3:
        F_val = np.array([f_numeric(point[0], point[1], point[2]), g_numeric(point[0], point[1], point[2]), q_numeric(point[0], point[1], point[2])])

    new_point = point - np.dot(J_inv, F_val)

    # Check for convergence
    if np.linalg.norm(F_val) < tolerance or np.linalg.norm(new_point - point) < tolerance:
        break
    else:
        point = new_point
        # Update the Jacobian matrix and its inverse if necessary
        if dimension == 2:
            J = np.array([[f_prime_x(point[0], point[1]), f_prime_y(point[0], point[1])],
                          [g_prime_x(point[0], point[1]), g_prime_y(point[0], point[1])]])
        elif dimension == 3:
            J = np.array([[f_prime_x(point[0], point[1], point[2]), f_prime_y(point[0], point[1], point[2]), f_prime_z(point[0], point[1], point[2])],
                          [g_prime_x(point[0], point[1], point[2]), g_prime_y(point[0], point[1], point[2]), g_prime_z(point[0], point[1], point[2])],
                          [q_prime_x(point[0], point[1], point[2]), q_prime_y(point[0], point[1], point[2]), q_prime_z(point[0], point[1], point[2])]])
        J_inv = np.linalg.inv(J)

if dimension == 2:
    intersection_point = (point[0].item(), point[1].item())
elif dimension == 3:
    intersection_point = (point[0].item(), point[1].item(), point[2].item())

print(f"computed intersection point is {intersection_point}")

