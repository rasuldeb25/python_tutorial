#logical operators = evaluate multiple conditions
#                   or = at least one condition must be True
#                   and = both conditions must be True
#                   not = inverts the condition

"""
#or
temp = int(input("What is the temperature outside?: "))
is_raining = input("Is it raining? (T/F): ")

if temp > 35 or temp < 0 or is_raining.upper() == 'T':
    print("Outdoor event is canceled")
else:
    print("Outdoor event is not canceled")
"""

"""
#and
temp = int(input("What is the temperature outside?: "))
is_sunny = input("Is it sunny outside? (T/F): ")

if temp > 28 and is_sunny.upper() == 'T': #here for the program to work properly it has to be OR operator.
    print("Outside is hot and sunny")
elif temp < 0 and is_sunny.upper() == 'F':
    print("Outside is cold and not sunny")
else:
    print("Outdoor event is not canceled")
"""

#not
temp = int(input("What is the temperature outside?: "))
is_sunny = input("Is it sunny outside? (T/F): ")

if not is_sunny.upper() == 'T':
    print(f"Outside is {temp}°C and it is not sunny outside.")
else:
    print(f"Outside is {temp}°C and it is sunny outside.")