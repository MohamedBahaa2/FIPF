from sympy import symbols, diff, sympify
from pyfiglet import Figlet
from  function_class import Function

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

