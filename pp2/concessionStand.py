#Concession stand program
#dictonary {key:value}

menu = {"pizza": 3.00,
        "burger": 2.5,
        "popcorn": 6.00,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 2.00,
        "water": 1.50,
        "nachos": 5.00}

cart = []
total = 0

print("----- MENU -----")
for key, value in menu.items():
    print(f"{key:10}:${value:.2f}")
print("-----------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food.lower() == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("----- YOUR ORDER -----")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")
print()
print(f"Total cart: ${total:.2f}")