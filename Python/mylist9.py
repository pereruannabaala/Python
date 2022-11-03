#Write a program that takes the date of birth of a person and the program outputs the age in terms of years,months,days TODAY.
import datetime  
birthday=input("What is your B'day? (in DD/MM/YYYY) ")  
birthdate=datetime.datetime.strptime(birthday,"%d/%m/%Y").date()
currentdate = datetime.date.today()
print("Your B'day is : "+birthdate.strftime('%d/%B/%Y'))
