# Inheritance is the capability of one class to derive or inherit the properties from some another class.
# single-inheritance


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


class Hier(Person):
    def __init__(self,name,age):
        self.age = age
        Person.__init__(self, name)  # 'name' here is referred as object of the class Person


a = Person("Nathan")  # creation of an object variable or an instance
print(a.getname())
emp1 = Person('mandy')  # an object of Person
print(emp1.isemployeer())
emp2 = Emp('nana')  # an object of Emp
print(emp2.isemployee())

emp3 = Emp('nama')
print(emp3.isemployeer())

# multiple inheritance


class Name1:
    def __init__(self):
        self.name1 = "alex"
        print("name one")


class Name2:
    def __init__(self):
        self.name2 = "martha"
        print("name two")


class DrivesOneTwo(Name1, Name2):
    def __init__(self):

        Name1.__init__(self)  # calling constructor of Name1
        Name2.__init__(self)  # Calling constructor of  Name2
        print("derived")
        print(self.name1, self.name2)


obj3 = Name1()
obj4 = Name2()
obj5 = DrivesOneTwo()


# Multilevel inheritance
class Base:
    def __init__(self, name):
        self.name = name

    def getname(self):
        return self.name


class Child(Base):
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age

    def getage(self):
        return self.age


class GrandChild(Child):
    def __init__(self, name, age, sex):
        Child.__init__(self, name, age)
        self.sex = sex

    def getsex(self):
        return self.sex


Grand = GrandChild("alex", 12, "male")
print(Grand.getname(), Grand.getage(), Grand.getsex())

'''
# Python program to demonstrate private members of the parent class 
class C(object): 
       def __init__(self): 
              self.c = 21
  
              # d is private instance variable  
              self.__d = 42    
class D(C): 
       def __init__(self): 
              self.e = 84
              C.__init__(self) 
object1 = D() 
  
# produces an error as d is private instance variable 
print (D.d)     '''

















