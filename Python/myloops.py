#In progamming you might need to do a repetitive task or access a value insidea list 
#even to generate in a range e.g 0 to 20, we use a loop

list1 = list(range(0,21))
print(list1)
for i in list1:
    if i % 5 == 0:
        print(i)
    else:
        pass

