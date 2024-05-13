# Basic file handelling method with read and write
from typing import List, Any

with open("my_new_file.txt", mode="r") as fileRead:
    content = fileRead.read()
    print(f"Content of the file is \n{content}")

x = open('myfile.txt', mode="w")
x.write('This is my file')
x.close()

a = 5
b = 10
if a <= b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is bigger than {b}")

stringVal = "Sandeep"

for x in stringVal:
    u = x.upper()
    print(f" value of x = {u}")

input_str = input("What is your name? ")
print(f"Hello {input_str}")

my_list = [2,3,4,5,6,7,9]
my_list.append(1)
print(my_list)
my_list.pop()

def myfunc(*args):
    '''
    This is one practise problem given on the tutorials, In this problem need to list out all the even numbers from the list of items passed into the *args,
    this is one demo of *args arguments usage
    :param args:
    :return:
    '''
    resultant_list= []
    for num in args:
        if num<=0:
            pass
        elif num % 2 == 0:
            print('The result of the division for each {} is {}'.format(num, num%2))
            resultant_list.append(num)
    return resultant_list

print(myfunc(-2,0,1,2,3,5,6,8,12,11))