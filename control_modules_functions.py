# Control Modules and functions

import mymodule
print(mymodule.add(5 ,3)) #output = 8

# The module mymodule is imported and the function add is called with arguments 5 and 3. The result is printed, which is 8.

#Basic import
import math
print(math.pi) #output = 3.141592653589793

#import with alias (as)
import numpy as np
print(np.arry([1, 2, 3])) #output = [1 2 3]

#importing specific functions or variable from a module
from math import sqrt, pi
print(sqrt(16)) #output = 4.0
print(pi) #output = 3.141592653589793

# import everything from a module
from math import *
print(sin(0)) #output = 0.0

#Functions 

def my_fun():
    print("Hello, World!*")
    
my_fun() #output = Hello, World!

# Types of functions
# 1. Built-in functions: are functions that are provided by Python and are always available for use. 
# #Examples include print(), len(), and type().

# 2. User-defined functions: are functions that are created by the user to perform specific tasks.
# Examples include functions defined using the def keyword.

# 3. Anonymous functions: (lambda functions) are functions that are defined without a name.
# They are created using the lambda keyword and are often used for short, simple operations.

# 4. Generator functions: are functions that use the yield keyword to return an iterator.
def my_generator():
    yield 1
    yield 2
    yield 3 #output = 1, 2, 3
    
# 5. Recursive functions: are functions that call themselves to solve a problem.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1) #output = 120
    
# Exception Handling with try,except, else and finally

# try block is used to test a block of code for error.if an error ocurred,the program will jump to the except block.
try:
    result = 10 / 0
except:
    print("An error occurred.") #output = An error occurred.
    
# except block used to handle specific error that ocurred in the try box.You can specify the type error 
# to catch , or generic except to catch all errors.
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by Zero!")
except Exception as e:
    print(f"An unexpected error ocurred: {e}" ) #output "Cannot devide by Zero"
    
#Else block
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by Zero!")
else:
    print(f"Division successful.")
    
# finally block

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by Zero!")
finally:
    print("This will always execute.")
    
#NoReturn
#when should you stick on NoReturn
# Always raise an exception , Never return , Terminating program (sys.exit())

from typing import NoReturn
def term_program():
    raise SystemExit("Terminating the program")




    