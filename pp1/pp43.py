#Magic methods = Dunder methods (double underscores) -__init__ __str__ __eq__
#               They are automatically called from Python's build-in operations
#               They allow developers to define of customize the behaviour of objects
from matplotlib.pyplot import title


class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __eq__(self, other):
        return  self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.price >= other.price

    def __gt__(self, other):
        return self.price <= other.price

    def __add__(self, other):
        return self.price + other.price
    def __contains__(self, keyword):
        return  keyword in self.title or keyword in self.author
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "price":
            return self.price
        else:
            return f"Key {key} not found"

book1 = Book(title="Python Tutorial", author="Brocode", price=1500)
book2 = Book(title="Java Tutorial", author="Hi code", price=2500)
book3 = Book(title="JS Tutorial", author="World code", price=2250)

print(book1)
print(book1 == book2)
print(book2 < book3)
print(book1 + book2)
print("Lion" in book3)
print(book1['price'])