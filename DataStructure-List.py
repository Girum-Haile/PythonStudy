# List- is a collection which is ordered, allow duplicated members and changeable
# list creation
list1 = [2, 3, 4, 5]
list2 = ['a', 'b', 'c']
# mixed type of values
list3 = ['a', 'b', 2]
# allow duplicated values
list4 = [2, 3, 4, 4, 2, 6, 6, 7, 8]

# accessing list
print(list1[0])  # we refer to the index number ot access the values
print(list1)
list10 = [['hell', 'heaven'], ['now']]
print(list10[0][1])  # accessing multi-dimensional list
# negative indexing -- it begins counting backward or beginning from end
print(list4[-3])
# to add new element to a list we use append() built-in function
list5 = [2, 4, 5, 5, 6]
print(list5)
list5.append(10)
print(list5)  # it will append 10 at the end of the list
# we can append another list
list5.append(list1)
print(list5)
# we can use extend() built-in function to add multiple elements at once
list7 = ['jack', 'rose', 21, 32]
print(list7)
list7.extend([5, 6, 7, 9])
print(list7)

# we use insert() built in function in order to add a new element at specific place
# insert(position, value)
list1.insert(0, 12)
print(list1)
# we use pop() built-in function in order to remove an element from a list using its index
list11 = [23, 45, 54, 66]
print(list11)
list11.pop(3)
print(list11)
# we use remove() built-in function in order to remove an element using the value it self
list12 = ['one', 'two', 'three']
print(list12)
list12.remove('one')
print(list12)
# slicing used to print specific range of elements from a list
list13 = [5, 6, 76, 32, 23, 45, 54, 66]
print(list13)
print(list13[1:4])  # prints the numbers from index 1 to 3 not including index 4
print(list13[:6])  # prints from the first index up to the 5th index
print(list13[2:])  # prints from the first index up to the last index
print(list13[:])  # prints all element
# negative slicing
list14 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
print(list14[-7:-1])
print(list14[::-1])  # reverse the list

list14.clear()  # clears the elements of the list
print(list14)
print(list13.index(5))  # prints out the index of the element
print(list4.count(4))  # it counts how many times that element appeared in the list
