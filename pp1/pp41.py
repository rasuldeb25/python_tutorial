#Static methods = a methods belongs to a class rather than any object from that class (instance)
#                   usually used for general utility functions

#Instance methods = best for operations on instances of class (objects)
#Static methods =   Best for utility functions that do not need access to class data

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_position = ["Manages", "Cashier", "Cook", "Janitor"]
        return position in valid_position

empolyee1 = Employee("Eugue", "Manager")
empolyee2 = Employee("Squidward", "Cashier")
empolyee3 = Employee("Spongebob", "Cook")

print(Employee.is_valid_position("Manages"))
print(empolyee1.get_info())