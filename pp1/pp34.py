#object  =  A "bundle" of related attributes (variables) and methods (functions)
#           ex, phone, cup, book
#           you need "class" to create many objects

#class = (blueprint) used to design the structure and layout of an object

from car_forpp34 import Car

car1 = Car("Mustang", 2024, "Black", False)
car2 = Car("Subaru", 1998, "Red", True)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)
car1.drive()
car1.stop()
car1.describe()

print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)
car2.drive()
car2.stop()
car2.describe()