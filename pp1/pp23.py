#return = statement used to end the function
#       and send the result back to the caller

"""
def add(x,y):
    z = x+y
    return z
def sub(x,y):
    z = x-y
    return z
def mult(x,y):
    z = x*y
    return
def div(x,y):
    z = x/y
    return z
print(add(3,4))
print(sub(3,4))
print(mult(3,4))
print(div(3,4))
"""

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last
full_name = create_name("rick","schansez")
print(full_name)