#temperature conversion program
unit = input("Is this temperature in Celsius or Fahrenheit (C/F)? ")
temp = float(input("Enter the temperature: "))

if unit.upper() == "C":
    converted = (temp * 9/5) + 32
    print(f"The temperature is {round(converted, 2)}°F")
elif unit.upper() == "F":
    converted = (temp - 32) * 5/9
    print(f"The temperature is {round(converted, 2)}C°")
else:
    print("Invalid unit")
