# Set is an unordered collection of data type that is iterable, mutable and has no duplicate elements.
# Set creation using 'set()' function
set1 = set("name")
print(set1)
set2 = {1, 2, 2, 3, 3, 4}  # it filters the duplicated value
print(set2)
set3 = {"a", 1, "b", 3}  # set with mixed value
# adding element to a set
# adds one element at a time
set4 = {1, 3, 4, 5}
print(set4)
set4.add(6)
print(set4)
# adding a multiple new element using update() built-in function
# it accepts list,strings and tuples
set4.update([7, 8, 9], "name")
print(set4)
# accessing a set
# it's not possible to access a set by referring their index since they are unordered
# accessing a set using a for loop
set5 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
for i in set5:
    print(i, end=' ' "\n")
# using 'in' keyword
print(1 in set5)
# deleting an element from a set
# using remove() or discard() built-in functions to delete set values
# deleting an element from a set using remove() function
#  it arises an error if the element is not present in the set
set6 = {1, 2, 3, 4, 5, 6, 7}
print(set6)
set6.remove(4)
print(set6)
set6.remove(98)
print(set6)  # prints 'KeyError'
# deleting an element using discard() method
set6.discard(6)
print(set6)
# using pop() function to remove only the last element
# If the set is unordered then there’s no such way to determine which element is popped by using the pop() function.
set7 = {66, 55, 77, 53}
set7.pop()
print(set7)
# using clear() function just to remove all the elements of  the set
set8 = {'a', 'b', 'c', 'd', 'e', 'f'}
print(set8)
set8.clear()
print(set8)
