# Operators

# Logical operators: They return a bool: and, or, not & is.
w = 4
x = 7
y = 4
z = 4

operatorAnd = w == z and y == z # operator and: All conditions must be met
operatorOr = x == z or y == z # operator or: At least one condition must be met
operatorNot = not True # Returns as true if the operator is false -- returns as false if the operator is true
operatorIs = x is z # Evaluates whether integer values ​​are equal

print(operatorAnd) # Screen output: True
print(operatorOr) # Screen output: True
print(operatorNot) # Screen output: False
print(operatorIs) # Screen output: False

# Relational operators: compare two expressions and return a bool: True o False
variableOne = 5
variableTwo = 20

mayor = variableOne > variableTwo
menor = variableOne < variableTwo
print(mayor) # Screen output: False
print(menor) # Screen output: True

# Arithmetic operators: of real numbers and integers: +, -, *, /, **, //, %.
a = 2
b = 5

sum = a + b # + 
subtraction = a - b # -
multiplication = a * b # *
division = a / b # /
exponent = a ** b # **
module = a % b # / %

print(sum)
print(subtraction)
print(multiplication)
print(division)
print(exponent)
print(module)


