#2d lists
"""
fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meat = ["chicken", "beef", "pork"]
groceries = [fruits, vegetables, meat]
"""

"""
["apple", "orange", "banana", "coconut"]
["celery", "carrots", "potatoes"]
["chicken", "beef", "pork"]

groceries = [["apple", "orange", "banana", "coconut"],
             ["celery", "carrots", "potatoes"],
             ["chicken", "beef", "pork"]]

for collection in groceries:
    for item in collection:
        print(item, end=" ")
    print()
"""

num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))
for row in num_pad:
    for column in row:
        print(column, end=" ")
    print()