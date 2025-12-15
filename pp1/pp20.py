#dictonary = a collection of {key:value} pairs
#               ordered and changeable. No duplicates

capitals = {"USA":"Washington DC",
            "India":"New Delhi",
            "China":"Beijing",
            "Russia":"Moscow"}

"""
country = input("Enter country: ")
if capitals.get(country):
    print(f"The capital of {country} is {capitals[country]}")
else:
    print("Not found")
"""
capitals.update({"Germany":"Berlin"})
#capitals.pop("China")
#capitals.popitem()
#capitals.clear()
#keys = capitals.keys()
#for key in keys:
#    print(key, end=" ")
#values = capitals.values()
#for value in values:
#    print(value, end=" ")

items = capitals.items()
for key, value in items:
    print(f"{key}: {value}")