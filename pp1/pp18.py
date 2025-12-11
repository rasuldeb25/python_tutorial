#collection = single 'variable' used to store multiple values
#List = []ordered and changeable. Duplicates OK
#Set = {}unordered and immutable, but add remove OK, NO duplicates
#Tuple = ()ordered and unchangeable. Duplicates OK, Faster
"""
#lists
fruits = ["apple", "orange", "banana", "coconut"]

print(dir(fruits))
print(len(fruits))
print(fruits[::2])
for fruit in fruits:
    print(fruit)
print("citrom" in fruits)
fruits[1] = "pineapple"
fruits.append("pineapple")
for fruit in fruits:
fruits.remove("apple")
fruits.insert(0,"pineapple" )
fruits.sort()
fruits.sort()
fruits.reverse()
fruits.clear()
print(fruits.index("apple"))
print(fruits.count("apple"))
print(fruits)
"""

"""
#sets
fruits = {"apple", "orange", "banana", "coconut"}
print(len(fruits))
fruits.add("pineapple")
fruits.remove("apple")
fruits.pop()
fruits.clear()
print(fruits)
"""


#tuples
fruits = ("apple", "orange", "banana", "coconut")
print(fruits.index("apple"))
print(fruits.count("apple"))
for fruit in fruits:
    print(fruit)
