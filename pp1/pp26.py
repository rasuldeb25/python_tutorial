#keyword arguments =  an argument preceded by an identifier
#                       helps with readability
#                       order of an arguments does not matter
#                       1. positional 2. default 3. KEYWORD 4. arbitrary
#*args = allows you to pass multiple no-key arguments
#*kwargs = allows you to pass multiple key arguments

"""
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,2,3,4,10))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")
display_name("Rick","Dr.","Schansez")


def print_address(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_address(street="12 Fakestreer",
                    city="Mars",
                    state="Missorio",
                    zip="001100",
                    apt="2112")
"""

def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for key, value in kwargs.items():
        print(f"{key}: {value}")
shipping_label("Dr.", "Rick", "Schansez", "II",
               street="12 Fake St.",
               apt = "1212",
               city="Detoriot",
               state="MI",
               zip="48127")