# Tuples they are more like lists but the main difference between them is tuples are immutable and hashable
# Tuple creation
tuple1 = (1, 2, 3, 4)
print(tuple1)
tuple2 = ('a', 'b', 'c', 'd', 'e')
print(tuple2)
# mixed type of elements
tuple3 = (1, 2, 3, 'a', 'b', 'c')
print(tuple3)
# allow duplicated elements
tuple4 = (1, 1, 2, 3)
print(tuple4)
# multi-dimensional tuple
tuple5 = (1, 2, 3, (34, 5))
# concatenation of tuples
# we use '+' sign to concatenate
print(tuple1 + tuple4)
# accessing tuples
print(tuple1[1])
print(tuple5[3][1])
# tuple slicing
tuple6 = (5, 6, 76, 32, 23, 45, 54, 66)
print(tuple6)
print(tuple6[1:4])  # prints the numbers from index 1 to 3 not including index 4
print(tuple6[:6])  # prints from the first index up to the 5th index
print(tuple6[2:])  # prints from the first index up to the last index
print(tuple6[:])  # prints all element
# negative slicing
tuple7 = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm')
print(tuple7[-7:-1])
print(tuple7[::-1])  # reverse the list
# IT'S NOT POSSIBLE TO APPEND ON TUPLE

# Tuples are immutable and hence they do not allow deletion of a part of it
# Entire tuple gets deleted by the use of del() method.
tuple8 = ('ab', 'ac', 'vb', 'ff')
print(tuple8)
del tuple8
# 'print(tuple8)' printing after deletion generates error

