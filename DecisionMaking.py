# if statement -It is used to decide whether a certain statement or block of statements will be executed or not.
# simple if statement
age = int(input("Enter your age: "))  # we use input() to get input from a user
if age <= 30:
    print("accepted")

#  nested if statement
name = input("enter name")
sex = input("enter sex")
if name == 'jack':
    if sex == 'male':
        print("your name is jack and your gender is male")
    else:
        print("your gender is not male")
else:
    print("you are not jack")


# if else statement

if age <= 30:
    print("accepted")
else:
    print("rejected")


# elif statement
num = int(input("enter number"))
if num > 0:
    print("positive number")
elif num < 0:
    print("negative number")
elif num == 0:
    print("zero")
else:
    print("invalid input")



