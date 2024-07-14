my_tuple = (1, 2, 3, 4,['a','b', 'c'])
print("The initial tuple is ", my_tuple)
print("Value in index zero", my_tuple[0])

'''
modifying the list inside the tuple
'''

my_tuple[4][1] = 'd'

print("The modified list inside the tuple is ", my_tuple)

'''
Another set of practice
'''

original_list = ['cup', 'cereal', 'milk', (8, 4, 3)]

tuple_val = original_list[3]

print(type(tuple_val))

count = len(tuple_val)
my_list = []
for c in tuple_val :
    my_list.append(c)

my_list.sort()
print(my_list)

original_list.pop(3)
original_list.append(my_list)
print(original_list)

