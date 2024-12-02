from sympy import symbols, diff, sympify,Matrix


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

if J.det() != 0:
    J_inv = J.inv()
else:
    print("Jacobian is singular at the point.")
    exit()

point = Matrix([[-2],       # guess point (x,y) = (1,1)
                [-3]])

new_point = list()

tolerance = 1e-6

while True:
    J_inv_val = J_inv.subs({x: point[0,0], y: point[1,0]}).evalf()
    F_val = F.subs({x: point[0,0], y: point[1,0]}).evalf()
    new_point = point - J_inv_val * F_val
    
    if F_val.norm() < tolerance or (new_point - point).norm() < tolerance:
        break
    else:
        point = new_point
        

print(point)