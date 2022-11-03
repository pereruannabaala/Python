def bmi(myweight, myheight):
    h2=myheight*myheight
    mybmi=myweight/h2
    
    return mybmi

myweight=int(input("Enter your weight in kilograms: "))
myheight=int(input("Enter your height in meters: "))
   

total=bmi(myweight,myheight)
print(total)
