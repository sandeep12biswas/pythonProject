"""
Default class sample
"""


class User:
    def __init__(self):
        self.nick_name = "Sample Name"
        self.city = "Sample City"
        self.__val = "private value"

    def introduction(self):
        print(f"Hi My name is {self.nick_name} and I live in {self.city} and the private property is {self.__val}")

    @classmethod
    def show(cls):
        print("this is class method")

    @staticmethod
    def another_method(self):
        print("This is static method")


sampleUser = User()

sampleUser.introduction()

sampleUser.nick_name = "Sandeep Biswas"
sampleUser.city = "Pune"

sampleUser.introduction()
