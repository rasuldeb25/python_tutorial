import math

from jinja2.lexer import float_re

#Ariphmetics operators
#Buil in math functions
"""
friends = 5

friends += 1
friends -=2
friends *= 2
friends /= 2
friends **=2
remainder = friends % 3

print(remainder)
"""

"""
x = 3.14
y = 4
z= 5

result = round(x)
result = abs(y)
result = pow(y,3)
result = max(x,y,z)
result = min(x,y,z)

print(result)
"""

"""
print(math.pi)
print(math.e)

x=128.1212

result  = math.sqrt(x)
result = math.ceil(x)

print(result)
"""

"""
radius = float(input('Enter the radius of the circle: '))
circumference = 2* math.pi * radius

print(f"The circumference of the circle is {round(circumference, 2)}cm")

"""

"""
radius = float(input('Enter the radius of the circle: '))
area = math.pi *pow(radius,2)

print(f"The area of the circle is {round(area, 2)}cm²")

"""

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a,2) + pow(b,2))

print(f"The hypotenuse is {round(c, 2)}cm")