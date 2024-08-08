"""
Exercise 1 (and Solution)
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells
them the year that they will turn 100 years old. Note: for this exercise, the expectation is that you explicitly write
out the year (and therefore be out of date the next year). If you want to do this in a generic way, see

"""
from datetime import date

name = input("Please input your name :")
age = input("please input your age:")

while not age.isnumeric():
    age = input("please input valid age: ")

year_to_hun = date.today().year - int(age) + 100

print(f"Hi {name}, in the year of {year_to_hun} you will become 100 years")
