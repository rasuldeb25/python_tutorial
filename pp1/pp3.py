#input() = A function that prompts a user to enter a data
#           Returns input as a String
"""
name = input("Your name?: ")
age = int(input("Your age?: "))
#age = int(age)
age = age + 1
print(f"Hello {name}!")
print("Happy birthday")
print(f"You are {age} years old!")
"""
#ex_1 rectangle area calculation
"""
lenght = float(input("Enter the lenght: "))
width = float(input("Enter the width: "))

area = lenght * width
print(f"The area is {area}cm².")
"""
#ex_2 shopping cart program
item = input("What you want to buy?: ")
price = float(input("Enter the price: "))
quantity = int(input("Enter the quantity: "))

total = price * quantity
print(f"You have bought {quantity} {item}(s).")
print(f"Total price: ${total}")
