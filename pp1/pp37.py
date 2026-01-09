#multiple inheritance = inherit from more than one parent class
#                       C(A,B)

#multilevel inheritance = inherit from a derived class (child class)
#                     C(B) <- B(A) <- A

class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f" {self.name} is eating")
    def sleep(self):
        print(f" {self.name} is sleeping")
class Prey(Animal):
    def flee(self):
        print(f" {self.name} flees")
class Predator(Animal):
    def hunt(self):
        print(f" {self.name} hunts")
class Rabit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey, Predator):
    pass

rabit = Rabit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabit.eat()