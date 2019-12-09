# Dictionary - is an order data collection of data values
# Dictionary holds key:value pair
# keys of dictionary must be unique and immutable and they are case sensitive

# Dictionary Creation
dict1 = {"name": "jack", "sex": "male"}
print(dict1)
dict2 = {"one": 1, "two": 2, "three": 3}
print(dict2)
# Mixed type of elements
dict3 = {"subject": "Python", "credit hour": 3, "letter": ['a', 'b', 'c']}
print(dict3)
# nested dictionary
dict4 = {"name": "alex", "age": 12, "pin": {"1": 10, "2": 20, "3": 30}}
print(dict4)
# accessing a value from a dictionary
print(dict1["name"])
print(dict1["sex"])
print(dict3["letter"][0])
print(dict4["pin"]["1"])
print(dict4.get("name"))  # using get() built-in method

# Adding a value into  a dictionary
dict4["sex"] = 'male'
print(dict4)
dict4["number"] = {1, 2, 3, 4}
print(dict4)
# deleting an element from a dictionary
# using 'del' key word
dict5 = {"animal": "dog", "type": "Doberman"}
print(dict5.keys())  # Returns list of dictionary keys
print(dict5)
del dict5["type"]
print(dict5)
del dict4["pin"]["1"]
print(dict4)
# deleting an element from a dictionary using 'pop()' function
dict6 = {"a": 1, "b": 2, "c": 3}
print(dict6)
dict6.pop("a")
print(dict6)
dict6.popitem()
print(dict6)
# we can use 'clear' function in order to delete the whole dictionary
dict7 = {"number": 1, "letter": "a"}
print(dict7)
dict7.clear()
print(dict7)