#Arthmetic Operators
#Addition
2+3
#Subtraction
2-3
#Multiplication
2*3
#Division
2/3
#Floor Division
2//3
#Modulus
2%3
#Exponentiation
2**3

#Assignment Operators
#Assigning a value to a variable
x = 5
#Addition Assignment
x += 3
#Subtraction Assignment
x -= 3
#Multiplication Assignment
x *= 3
#Division Assignment
x /= 3
#Floor Division Assignment
x // 6
#Modulus Assignment
x %= 3
#Exponentiation Assignment
x **= 4

#Comparision Operators
#Equal
x == 2
#Not Equal
x != 2
#Greater Than
x > 2
#Less Than
x < 2
#Greater Than or Equal To
x >= 2
#Less Than or Equal To
x <= 2

#Logical Operators
x = 5
#AND
#Returns True if both statements are true
x > 3 and x < 6
#OR
#Returns True if one of the statements is true
x > 3 or x < 6
#NOT
#Reverse the result, returns False if the result is true
not(x > 3 and x < 6)

#Identity Operators
#is
#Returns True if both variables are the same object
x is y
#is not
#Returns True if both variables are not the same object
x is not y

#Membership Operators
#in
#Returns True if a sequence with the specified value is present in the object
x in y
#not in
#Returns True if a sequence with the specified value is not present in the object
x not in y

#Bitwise Operators
a = 10
b = 4
#AND
#Sets each bit to 1 if both bits are 1
result = a & b # output is 0 (in binary 0000)
#OR
#Sets each bit to 1 if one of the bits is 1
result = a | b # output is 14 (in binary 1110)
#XOR
#Sets each bit to 1 if only one of the bits is 1
result = a ^ b # output is 14 (in binary 1110)
#NOT
#Inverts all the bits
result = ~a # output is -11
#Left Shift
#Shift left bites to the left,filling with zero from the right.
result = a << 1 # output is 20
#Right Shift
#Shift bits to the right.
result = a >> 1 # output is 5

