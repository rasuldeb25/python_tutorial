#working with strings
#name = input("Enter you full name: ")
#phone = input("Enter your phone number: ")
"""
result = len(name)
result = name.find("A")
result = name.rfind("o")
name = name.capitalize()
name = name.upper()
name = name.lower()
result = name.isdigit() #only return true when all of them are digits
result = name.isalpha() #only return true when all of them are letters
result = str(phone).count("-")
result = phone.replace("-", " ")
print(result)
"""
#VALIDATE_USER_INPUT
#1. username is no more than 12 characters
#2. username must not contain spaces
#3. username must not contain digits

username = input("Enter a username: ")
username.find(" ")
username.isalpha()
if len(username) > 12:
    print("Username is too long")
elif not username.find(" ") == -1:
    print("Username cannot contain spaces")
elif not username.isalpha():
    print("Username cannot contain digits")
else:
    print(f"Welcome {username}!")