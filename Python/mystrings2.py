firstname = input("Enter your first name: ")
firstname = firstname.strip()
firstname = firstname.upper()

lastname = input("Enter your last name: ")
lastname = lastname.strip()
lastname = lastname.upper()

email = input("Enter your email: ")
email = email.strip()
email = email.lower()
print(email)

fullname = firstname +" "+ lastname
print(fullname)