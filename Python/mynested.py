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