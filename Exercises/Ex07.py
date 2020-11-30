# Password system

f = True
while f == True :
    contra = "hola123"
    print("enter your password")
    a = input()
    if a == contra:
        print("Welcome to the system")
        f = False
    else:
        print("Wrong password, do you want to try again?")
        b = input()
        if b == "yes":
            f = True
        else:
            f = False