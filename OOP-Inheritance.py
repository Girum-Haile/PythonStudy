# Inheritance is the capability of one class to derive or inherit the properties from some another class.
class Person:
    def __init__(self, name):
        self.name = name

    def getname(self):
        return self.name

    def isemployeer(self):
        return False


class Emp(Person):  # class emp inherits class person
    def isemployee(self):
        return True


emp1 = Person('mandy')  # an object of Person
print(emp1.isemployeer())
emp2 = Emp('nana')  # an object of Emp
print(emp2.isemployee())

emp3 = Emp('nama')
print(emp3.isemployeer())








