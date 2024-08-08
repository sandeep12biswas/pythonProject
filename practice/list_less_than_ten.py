"""
take a list for example   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
and write a program that prints out all the elements of the list that are less than 5.

"""
lst = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

new_lst = []

for val in lst:
    if val < 5:
        new_lst.append(val)

print(f"The list {new_lst} contains values less than 5")