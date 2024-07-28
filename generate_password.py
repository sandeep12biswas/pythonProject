'''

This program will generate random password for users based ont he input the user will provide
'''

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y']
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
spl_char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']
firsst_choice__opt = ['1', '2']

str_choice = ''' --- Password Generator ---
Choice option :
1 : Generate password
2 : Exit from the program
Your choice : '''

print(str_choice)
first_choice = input()

while not firsst_choice__opt.__contains__(first_choice):
    print("please enter correct option between 1 and 2")
    first_choice = input()

if first_choice == '2':
    print("You opted to quit the password generation ! Bye")

print("Please provide the password length! :")
pwd_length = input()
while not pwd_length.isnumeric():
    print(f"please enter valid length! {pwd_length} is not valid integer value")
    pwd_length = input()

print("Use upper case letter! (Y/N)")
upper_case = input()
print(upper_case.upper() != 'y'.upper())
while upper_case.upper() != 'y'.upper() and upper_case.upper() != 'n'.upper():
    print("Please select Y or N :")
    upper_case = input()

print("Use digit ! (Y/N)")
upper_case = input()
while upper_case.upper() != 'y'.upper() and upper_case.upper() != 'n'.upper():
    print("Please select Y or N :")
    upper_case = input()

print("Use special character ! (Y/N)")
upper_case = input()
while upper_case.upper() != 'y'.upper() and upper_case.upper() != 'n'.upper():
    print("Please select Y or N :")
    upper_case = input()
