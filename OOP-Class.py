# class - creates user defined data structure.
# class is like a blue print of an object
# class creation


class New:
    pass



class Dogs:
    type = "Doberman" # class attributes
    atr = "mamal"

    def method(self):
        print("Dog breed:", self.type)
        print("Dog atr:", self.atr)


Dog1 = Dogs()  # object instantiation
Dog1.method()  # accessing class attributes


class Person:
    def __init__(self, name, age):  # '__init__'- Constructors are used to initialize the object’s state.
        self.name = name
        self.age = age

    def name_age(self):
        print(f'Hello {self.name} you are {self.age} years old'.format(self.name, self.age))


person1 = Person("girum",12)
person1.name_age()





