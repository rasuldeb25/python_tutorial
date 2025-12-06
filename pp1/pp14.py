#while loop = executes some code WHILE some condition if TRUE

"""
name = input("Enter your name: ")
while name == "" or name.isdigit():
    print("You didn't enter a name.")
    name = input("Enter your name: ")
print(f"Hello {name}!")

age = int(input("Enter your age: "))
while age < 0 or age > 100:
    age = int(input("Enter your age: "))
print(f"You are {age} years old.")

food = input("Enter food you like: ")
while not food.lower() == "q":
    print(f"You like {food}")
    food = input("enter food you like (q to quit): ")
print("Thank you!")
"""
num = int(input("Enter a number between 1-10: "))
while num < 1 or num > 10:
    print("Invalid number")
    num = int(input("Enter a number between 1-10: "))
print(f"You entered {num}")