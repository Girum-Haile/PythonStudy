# Polymorphism -same function name but different signature
# polymorphism with class method


class Ethiopia():
    def capital(self):
        print("Addis Ababa is the capital of Ethiopia.")

    def language(self):
        print("Amharic the primary language of Ethiopia.")

    def type(self):
        print("Ethiopia is a beautiful country.")


class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")


obj_ind = Ethiopia()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()

# polymorphism with inheritance
# method overriding-is the process of re-implementing the method in child class which is inherited from the parent class
class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")


class sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")


class ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")


obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()

