class Student:

    def __init__(self):
        self.__first_name = None
        self.__last_name = None

    def getterFirst_name(self):
        return self.__first_name

    def setterFirst_name (self, first_name):
        self.__first_name = first_name

    def getterLast_name(self):
        return self.__last_name
    def setterLast_name (self, last_name):
        self.__last_name = last_name

    def show_name (self):
        print(f"Name is {self.__first_name} {self.__last_name}")



std = Student()
std.setterFirst_name("Sandeep")
std.setterLast_name("Biswas")


std.show_name()
