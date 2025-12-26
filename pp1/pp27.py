#Iterables = An object/collection that can return its element one at a time
#           allowing it iterated over in a loop


"""
numer = [1,2,3,4,5]
for number in reversed(numer):
    print(number, end=" ")


numer = (1,2,3,4,5)
for number in numer:
    print(number, end=" ")

fruits = {"apple", "banana", "cherry", "orange", "kiwi"}
for fruit in fruits:
    print(fruit, end=" ")

name = "Bro Code"
for letter in name:
    print(letter, end=" ")
"""

my_dic = {"A":1, "B":2, "C":3, "D":4, "E":5}
for key, value in my_dic.items():
    print(f"{key}: {value}")