#Write a program that takes input of someone's basic salary and benefits, adds them to find the gross salary then uses  the gross salary to find the NHIF.To find the Kenya NHIF Rate using THIS LINK:  
basicsalary=int(input("Enter basic salary"))
benefits=int(input("Enter benefits"))
gross_salary=int(basicsalary)+int(benefits)
print(gross_salary)
if (gross_salary <= 5,999):
    print("150")
elif (gross_salary >= 6000) and (gross_salary <=7,999):
    print("300")
elif (gross_salary >= 6000) and (gross_salary <=7,999):
    print("400")
elif (gross_salary >= 8000) and (gross_salary <=11,999):
    print("500")
elif (gross_salary >= 12000) and (gross_salary <=14,999):
    print("600")
elif (gross_salary >= 15000) and (gross_salary <=19,999):
    print("750")
elif (gross_salary >= 20000) and (gross_salary <=24,999):
    print("850")
else:
    print("900")
