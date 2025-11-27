#Pyhton weight converter

weight = float(input("Enter your weight: "))
unit = input("(L)bs or (K)g: ")

if unit == "K":
    converted = weight * 2.204
    print(f"You are {round(converted, 2)} pounds")
elif unit == "L":
    converted = weight / 2.20
    print(f"You are {round(converted, 2)} kilos")
else:
    print("Invalid unit")