


class Vehicle:


    def __init__(self):
        pass
    def go(self):
        print("Going!")

    def introduce(self):
        print("I am Vehicle")

class Flyable:
    def __init__(self):
        pass

    def fly(self):
        print("Flying!")

    def introduce(self):
        print("I am Vehicle")

class Airplan(Vehicle, Flyable):

    pass


"""
my_plan = Airplan()
my_plan.go()
my_plan.fly()
my_plan.introduce()
print(Airplan.__bases__)
"""




class Dog:
    latin = 'canis'

    def __init__(self, colour='brown'):
        self.colour = colour
        Dog.latin += colour

"""
print(Dog.latin)
first = Dog()
print(Dog.latin)
second = Dog('red')
print(second.latin)
third = Dog('white')
print(second.latin)
"""


class X:
    def __init__(self):
        pass


"""
x = X('myobject')
print(x.self)
"""
