#IF ELSE Statement
average = 70
if (average > 50) and (average < 100):
    print("Pass")
else:
    print("Fail")







#IF ELIF Statement
#It is used to check more than 2 possible conditions
grades =int(input("Enter grades: "))
if (grades >=80) and (grades <100):
    print("A")
elif (grades >=70) and (grades <80):
    print("B")
elif (grades >=60) and (grades <70):
    print("C")
elif (grades >=50) and (grades <60):
    print("D")
else:
    print("F")



#Nested IF
m = input("Enter number")

try:
    m = int(m)
    if m < 0 or m > 100:
        print("Marks out of range")
    else:
        if m < 50:
            print("Fail, you repeat")
        else:
            print("Passed, Proceed to next class")
except:
    print("Ensure you enter a number")