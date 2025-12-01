#conditional expression  = A one-line shortcut for the else-if statement (ternary operator)
#                           Print or assign one of two values based on the condition
#                           X if condition else Y

"""
num = float(input("Enter a number: "))
print("Positive" if num > 0 else "Negative")
result = "Even" if num %2 == 0 else "Odd"
print(result)

a = float(input("Enter a number: "))
b = float(input("Enter another number: "))
maxNum = a if a>b else b
minNum = b if b<a else a
print(f"The maximum number is {maxNum}")
print(f"The minimum number is {minNum}")

age = int(input("Enter an age: "))
status = "adult" if age >=18 else "teenager"
print(f"You are {age} years old and you are a {status}")


temp = int(input("What is the temperature outside?: "))
temp = "It is hot outside." if temp > 30 else "It is NOT hot outside."
print(temp)
"""

for _ in range(3):
    adminPassword = int(input("Enter the admin password: "))
    accessGrant = "You are an admin" if adminPassword == 1234 else "You are not an admin"
    print(accessGrant)
    if adminPassword == 1234:
        break