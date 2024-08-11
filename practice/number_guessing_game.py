"""
Guessing Game One
Exercise 9 (and Solution)
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""
from random import random, randint

ext = ""
attempted = 0
correct_guess = 0
while not ext.upper() == "Q":

    num = ''
    while not num.isdigit():
        num = input("guess any number between 1 to 9 : ")

        num = int(num)

        random_number = randint(1, 9)
        attempted = + 1
        if num == random_number:
            correct_guess = + 1
            print(f"You have guessed it right the number is {random_number}")
        else:
            print("Ah! sorry wrong guess, try again")

    #input("Do you want to quit? type 'q'")
    print(f" your total attempt is {attempted} and you have guess correct {correct_guess} times")
