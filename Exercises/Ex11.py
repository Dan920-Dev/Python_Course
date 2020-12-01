# Salary calculator

print("Enter your name: ")
name = str(input())
print("Enter your DUI: ")
dui = input()
print("Enter your NIT: ")
nit = input()
print("Enter your salary: ")
salary = float(input())
print("Enter your voucher if you have it")
voucher = float(input())
 
# Calculated
afp = salary * 0.0725
isss = salary * 0.15
rent = salary * 0.10
mont = voucher + salary
desc = afp+isss+rent
print(name, " with number of DUI:", dui, "and number of NIT:",nit)
print("total discount: $", desc)
print("Net salary to receive: $",mont-desc)

