# converter (pounds, kilos, dollars and euros)

def menu():
    print("1. Convert Pounds to Kilos")
    print("2. Convert Kilos to Pounds")
    print("3. Convertir Euros a Dollars")
    print("4. Convert Dollars to Euros")
    print("Press any option other than the above to exit")
    print("Select an option from the menu: ")
    opcion = input()
    opcion = int(opcion)
    if opcion==1: libras_kilos()
    elif opcion==2: kilos_libras()
    elif opcion==3: Eu_dolares()
    elif opcion==4: Dolares_Eu()
    else: print("You have logged out") , exit()


def libras_kilos():
    print("enter the number of pounds to convert to kilos:")
    libras = float(input())
    resultado = libras/ 2.2046
    print(libras , "libras are " , resultado , "kilogramos")
    menu()
    
def kilos_libras():
    print("enter the number of kilos to convert to books: ")
    kilos = float(input())
    resultado = kilos * 2.2046
    print(kilos , "kilos are " , resultado , "pounds")
    menu()

def Eu_dolares():
    print("enter the amount of euros to convert to dollars:")
    euros = float(input())
    resultado = euros * 1.0831
    print(euros , "euros are $" , resultado , "dolares")
    menu()

def Dolares_Eu():
    print("type the amount of dollars to convert to euros:")
    dolares = float(input())
    resultado = dolares *  0,9233 
    print(dolares , "dollars are" , resultado , "euros")

menu()
