#Write a program that takes as input the speed of a car e.g 80. If the speed is less than 70, it should print “Ok”. Otherwise, for every 5 km/s above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points.
speed = int(input("Enter speed: "))
if speed <70:
    print("okay")
elif (speed >=70) and (speed <=75):
    print("1 point")
elif (speed >=75) and (speed <=80):
    print("2 points")
elif (speed >=80) and (speed <=85):
    print("3 points")
elif (speed >=85) and (speed <=90):
    print("4 points")
elif (speed >=90) and (speed <=95):
    print(" 5 points")
elif (speed >=95) and (speed <=100):
    print("6 points")
elif (speed >=100) and (speed <=105):
    print("7 points")
elif (speed >=105) and (speed <=110):
    print("8 points")
elif (speed >=110) and (speed <=115):
    print("9 points")
elif (speed >=115) and (speed <=120):
    print("10 points")
elif (speed >=120) and (speed <=125):
    print("11 points")
elif (speed >=125) and (speed <=130):
    print("12 points")
else:
    print("license suspended")