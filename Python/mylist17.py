#Write a program that takes input of 2 values and adds them. The program should only accept numbers and floats only or otherwise display an error “invalid character entered” and take the user to re-enter the inputs
x=input("Enter number")
y=input("Enter number")
z=(x+y)
try:
    if x=int() and y=int():
        print(z)
    else:
        if x=float() and y=float():
            print(z)
        else:
            print("Invalid character entered")
except:
    print("Ensure the number is an integer or float")