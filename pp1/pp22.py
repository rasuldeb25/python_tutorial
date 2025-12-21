#functions = a block of code which is executed only when it is called
#           place() after the function name to invoke it

"""
def happy_birthday(name, age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print("Happy birthday to you!")
    print()

happy_birthday("Rick",23)
happy_birthday("Alex", 23)
happy_birthday("Fed", 23)
"""

def display_invoice(username, amount, due_date):
    print(f"Hello {username}!")
    print(f"Your bill of ${amount:.2f} is due {due_date}")
display_invoice("Rick", 42.23,"01/01/2023")
display_invoice("Alex", 23.21, "01/01/2024")

