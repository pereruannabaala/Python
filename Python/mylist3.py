#Write a program which gets a phone number from a form input or terminal. Validates the phone number by checking if it starts with +254.. or 07.. or 71… or 254.. or 01... Convert the number to start with +254… 
mynumber = (input("Enter your phone number: "))
if '07' in "mynumber":
    print ('wrong number')
else:
    myphone = "+254" + str(mynumber)
    print (myphone)
if '71' in "mynumber":
    print ('wrong number')
else:
    myphone = "+254" + str(mynumber)
    print (myphone)
if '254' in "mynumber":
    print ('wrong number')
else:
    myphone = "+254" + str(mynumber)
    print (myphone)
if '01' in "mynumber":
    print ('wrong number')
else:
    myphone = "+254" + str(mynumber)
    print (myphone)

