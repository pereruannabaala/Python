#Implement a program that takes 3 form inputs or from the terminal, and stores them in three variables. Return the largest of the three. Do this without using the the inbuilt max () function!
a = int(input("Enter number: "))
b = int(input("Enter number: "))
c = int(input("Enter number: "))

if a > b and a > c:
    print("a is the largest")
elif b > a and b > c:
    print("b is the largest")
else:
    print("c is the largest")

