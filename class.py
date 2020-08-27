import sys

class Person:
    name = None
    age = None
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        return self.name

    def print_age(self):
        return self.age

me = Person('john', 32)
print ('My name is ', me.name)
print ('My age is', me.age)
