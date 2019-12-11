# A loops are instructions that repeats until a specified condition is reached.
# for loop - runs for a present number of times
# for in loop using range
for i in range(10):
    print(i)  # print from 0-9

for i in range(1, 11):  # it prints the values starting from 1 up to 10
    print(i)

for i in range(2, 11, 3):  # prints out by adding 4 to each number up to the range
    print(i)

for i in range(5):
    print("hello world")

lit4 = ['a', 'b', 'c', 'd', 'e']  # iterates over a list
for i in lit4:
    print(i)
lit5= ['ab', 'bc', 'cd', 'de', 'fe']  # iterating over an index
for index in range(len(lit5)):
    print(lit5[index])
# nested for in loop
for i in range(1, 5):
    for j in range(i):
        print(j, end='')
    print()

