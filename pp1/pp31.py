#modules = a file containing code you want to include in your program
#           use 'import' to include a module (build-in or your own)
#           useful  to break up a large program reusable separate files

"""
import math
import math as m
print(math.pi)
from math import pi
print(pi)
print(m.pi)
"""
import example_module
result = example_module.pi
print(result)
result = example_module.square(5)
print(result)
result = example_module.cube(5)
print(result)
result = example_module.circumference(5)
print(result)
result = example_module.area(5)
print(result)
print(example_module.pi)