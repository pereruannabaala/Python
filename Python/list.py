#1. Display 2 using index, from the list.
mylist=["hello",90,100.5,True,]
print(mylist[3])
mylist[0]= "good morning"
print(mylist)

#2. Output James  using index, from the list.
trainees = ["John",[2,["James","Mary"]]]
print(trainees[1][1][0])

#3. Using a method add 56 at the end of the list.
trainees[1][1].insert(3, "56")
print(trainees)

#4. Using a method add the name Mike between James and Mary
trainees[1][1].insert(1, "Mike")
print(trainees)

#5. Change the value of 2 to 8
trainees[1][0]=8
print(trainees)

#6. Remove John and Mary from the list
del trainees[1][1][1]
print(trainees)

#6. Remove John and Mary from the list
del trainees[0]
print(trainees)   

#6. Remove John and Mary from the list.
