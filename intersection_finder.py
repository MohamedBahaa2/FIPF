from sympy import symbols, diff, sympify,lambdify,Matrix
import numpy as np

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
dimension = int(input("please enter the number of functions, options: [2,3]:  "))

input_f = input("Function 1: ")
input_g = input("Function 2: ")

if dimension == 3:
    input_q = input("Function 3: ")

x,y,z = symbols("x y z")  # define variables

f = sympify(str(input_f)) # function 1
g = sympify(str(input_g)) # function 2
if dimension == 3:
    q = sympify(str(input_q))

if dimension == 2:
    F = Matrix([[f],          # F-matrix (original functions matrix)
                [g]])

    J = Matrix([[diff(f,x),diff(f,y)],
                [diff(g,x),diff(g,y)]])
    point = np.array([1,1])
    
if dimension == 3:
    F = Matrix([[f],          # F-matrix (original functions matrix)
                [g],
                [q]])

    J = Matrix([[diff(f,x),diff(f,y),diff(f,z)],
                [diff(g,x),diff(g,y),diff(g,z)],
                [diff(q,x),diff(q,y),diff(q,z)]])
    point = np.array([1,1,1])
    
if J.det() == 0:
    print("Jacobian is singular at the point.")
    exit()



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

while True:
    if dimension == 2:
        J = np.array([[f_prime_x(point[0], point[1]), f_prime_y(point[0], point[1])],
                    [g_prime_x(point[0], point[1]), g_prime_y(point[0], point[1])]])
        
    
        F_val = np.array([f_numeric(point[0], point[1]), g_numeric(point[0], point[1])])

        
    if dimension == 3:
        J = np.array([[f_prime_x(point[0], point[1], point[2]), f_prime_y(point[0], point[1], point[2]), f_prime_z(point[0], point[1], point[2])],
                      [g_prime_x(point[0], point[1], point[2]), g_prime_y(point[0], point[1], point[2]), g_prime_z(point[0], point[1], point[2])],
                      [q_prime_x(point[0], point[1], point[2]), q_prime_y(point[0], point[1], point[2]), q_prime_z(point[0], point[1], point[2])]])
        
    
        F_val = np.array([f_numeric(point[0], point[1], point[2]), g_numeric(point[0], point[1], point[2]), q_numeric(point[0], point[1], point[2])])

        
    J_inv = np.linalg.inv(J)    
    new_point = point - np.dot(J_inv, F_val)

    # Check for convergence
    if np.linalg.norm(F_val) < tolerance or np.linalg.norm(new_point - point) < tolerance:
        break
    else:
        point = new_point
        
if dimension == 2:
    intersection_point = (round(((point[0])).item()), round((point[1]).item()))
if dimension == 3:
    intersection_point = (round(((point[0])).item()), round((point[1]).item()), round((point[2]).item()))
    
print(f"computed intersection point is {intersection_point}")

