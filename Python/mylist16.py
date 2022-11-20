#Write a program that takes the email and password as input from a user and checks if they are equal to “admin@mail.com” and password is “Admin@123” , if so then return user “Login is Successful” and ONLY accepts 3 tries after which it notifies you that you have been blocked.
attempts = 0

while attempts < 3:
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    if username == 'admin@mail.com' and password == 'Admin@123':
        print('You have successfully logged in.')
        break
    else:
        print('Incorrect credentials')
        attempts += 1
        continue