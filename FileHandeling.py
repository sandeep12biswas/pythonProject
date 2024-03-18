# Basic file handelling method with read and write

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

