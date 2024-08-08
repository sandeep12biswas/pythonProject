"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.
"""

lst1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


final_lst = []
smaller_lst = []
larger_lst = []
if len(lst1) >= len(lst2):
    larger_lst = lst1
    smaller_lst = lst2
else:
    larger_lst = lst2
    smaller_lst = lst1

for val in larger_lst:
    if smaller_lst.__contains__(val) and not final_lst.__contains__(val):
        final_lst.append(val)

print("The final list is {}".format(final_lst))

