# a function is a named sequence of statements that performs a computation
# built-in functions
import math
print(math.sqrt(25))
# user defined functions
# defines a fun 'hello()'


def hello():
    print("hello world")
# function call


hello()
# function with parameter


def add(a, b): # 'a' and 'b' are called parameters
    return a+b


print(add(2, 3))  # '2' and '3' are called arguments

# default argument-are those that take a default value if no argument value is passed during the function call.


def sub(a, b=4):
    return a-b


print(sub(a=7))
print(sub(7, 5))
print(sub(a=4, b=2))  # keyword argument


def add(*args):  # we use ' *args ' for variable number of arguments or any other word in place of args
    print(sum(args))


add(2, 3, 4, 5, 5)

''' Anonymous functions are also called lambda functions 
in Python because instead of declaring them with the standard def keyword, you use the lambda keyword.'''


add = lambda x: x+2 # 'x' is the parameter and 'x+2' the expression
print(add(2))


def print_name(name):
    print(f'Your name is: {name}'. format(name))


def main():
    print_name("Jack")


if __name__ == '__main__':main()  # __init__ function that initializes an instance of a class or an object.







