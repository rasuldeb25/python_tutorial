#Inheritance =  Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extendability
#               class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

class Mice(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

dog = Dog("Reks", "sheepherd")
cat = Cat("Heye", "Pink")
mice = Mice("Jim", "blue")

print(dog.name)
print(dog.breed)
print(dog.is_alive)
print(cat.name)
print(cat.color)
print(cat.is_alive)
print(mice.name)
print(mice.color)
print(mice.is_alive)
