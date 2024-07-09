name = "Python is a wonderful scripting language"
num = "12345678910"
print(len(name))

print(name[-40])

c = name.upper()
print(c)
print(name.upper())

sentence = "The sum of {1} and {0} is {2}".format(10,20,(10+20))
print(sentence)

'''
In the below statement two list are there, the ask is to sort them and slice them and put in final list in such form the 
output should match ['d', 'b', 'a', 3, 2, 1]
'''

my_list = ['b', 'd', 'a', 'z', 'x']

another_list = [1, 2, 3, 4, 5]

my_list.sort()
my_list.reverse()
another_list.reverse()
final_list = my_list[2:] + another_list[2:]

print(final_list)