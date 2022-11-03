#Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40
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
