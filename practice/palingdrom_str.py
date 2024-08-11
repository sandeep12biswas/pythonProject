palin  = input("Please enter any string to check if this is palindrome : ")

pal_list = []
reverse_palin = []
for ch in palin:
    pal_list.append(ch)
    reverse_palin.append(ch)

reverse_palin.reverse()
if pal_list == reverse_palin:
    print(f"String {palin} ia palindrome")
else:
    print(f"String {palin} ia is not palindrome")
