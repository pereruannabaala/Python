#Write a program that prints the largest of 4 inputs taken in from a user. Assume that the user would not enter any two numbers which are the same.

a=int(input("Enter number"))
b=int(input("Enter number"))
c=int(input("Enter number"))
d=int(input("Enter number"))

if a>b and a>c and a>d:
    print("a is the largest number")
elif (b>a) and (b>c) and (b>d):
    print("b is the largest number")
elif (c>a) and (c>b) and (c>d):
    print("c is the largest number")
else:
    print("d is the largest number")










