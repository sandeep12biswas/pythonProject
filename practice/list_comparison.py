"""
Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python
that takes this list a and makes a new list that has only the even elements of this list in it.

"""

a = [1, 4, 4, 5, 5,9, 9, 16, 25, 36, 49, 64, 81, 100]

unique_lst = []
for num in a:
    if not unique_lst.__contains__(num):
        unique_lst.append(num)

print(f"Unique list is {unique_lst}")

"""
THis is another option to conversion, where list is first converted to set and then the same is converted back to list, 
in this way the unique list can be achieved 
"""
my_set = set(a)
print(f"Unique set is {my_set}")

lst = list(my_set)
print(f"Unique list is {lst}")
