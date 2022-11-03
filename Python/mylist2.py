#Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display  either “odd” or “even” to the user.Hint: how does an even / odd number react differently when divided by 2?

number = int(input("Enter Number: "))
if number % 2 == 0:
    print("even")

#If the number is a multiple of 4, display out a different message.
if number % 4 == 0:
    print("multiple of 4")
else:
    print("odd")

