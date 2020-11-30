# Investment of money

print("Welcome to the investment system ")
print("Enter its present value in dollars")
valor= float(input())
print("Enter interest: ")
interes = float(input())
print("Enter the period: ")
PERIODO = float(input())


CAPITAL = (valor)* pow((1+(interes)),PERIODO)

print("Its capital is  : ",CAPITAL)