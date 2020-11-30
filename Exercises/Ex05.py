# Calculate grade point average
"""

"""
print("Enter how many notes you want to enter: ")
cantNotas = input()
suma = 0

arregloNotas = [0 for i in range(int(cantNotas))]
for i in range(len(arregloNotas)): 
    print("Enter the note: " ,i+1)
    arregloNotas[i] = float(input())

for i in range(len(arregloNotas)):
    suma = suma + arregloNotas[i]

resultado = suma/len(arregloNotas)
print(resultado)
