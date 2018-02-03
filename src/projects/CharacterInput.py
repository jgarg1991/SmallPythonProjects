# This program takes AGE as input and prints the year in which you turn 100 yrs old.
import datetime


name = input("What is your name? : ")
age = int(input("What's your age? : "))
currentyear = datetime.datetime.now().year
print("Current year is : ", currentyear)

print("You will turn 100 yrs old in : ", (currentyear - age) + 100)