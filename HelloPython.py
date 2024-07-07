# Comments can be given in this way starting with # at the beginning


print("Hello Python and hello PCAP")
a = 50
print(type(a))
print(id(a))

a = 100
print(type(a))
print(id(a))


def __init__(self=None):
    print(self)


__init__()

strValue = "My name is Sandeep"

postSplit = strValue.split(" ") # This is same as strValue.split(), because it splits on white space by default
print(postSplit)
print(" postSplit variable type is", type(postSplit))
print("The value postString split is {}".format(type(postSplit)))

print(strValue.upper())
print(strValue)

# Sorting String values

nameList = ["Sandeep", "Mishika", "Alpana" , "Mousumi"]
#nameList.__setitem__(4,"Ashok")
nameList.sort()
sortedNameList = nameList
print(f"Sorted Name comes like {sortedNameList}")

myDisc = {}
myDisc.__setitem__("name","Sandeep")
print(myDisc)