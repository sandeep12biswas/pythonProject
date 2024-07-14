# Assignment 1

"""
Print Bill's salary from the dictionary

"""

my_list = [{'Tom' : 20000, 'Bill' : 12000}, ['car', 'laptop', 'tv']]

print_state = "Bill's salary is {}".format(my_list[0]['Bill'])

print(print_state)

print(my_list[0].get('Bill'))

bill_salary = f"Bill's salary is {my_list[0].get('Bill')}"

print(bill_salary)