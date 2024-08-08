"""

Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""

divisor = input("Please enter whole number: ")

while not divisor.isdigit():
    divisor = input("Please input valid number: ")

divisor = int(divisor)

div_list = []
for i in range(1, divisor):
    if divisor % i == 0 and i >1:
        div_list.append(i)

print(f"{div_list} are the list of number can divide {divisor} equally ")
