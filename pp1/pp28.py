#Membership operators = used to test whether a value or variable is found in sequence
#                       (string, list, tuple, set or dictionary)
#                       in =
#                       not in =

"""
word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"There is no {letter}")

if letter not in word:
    print(f"There is no {letter}")
else:
    print(f"There is a {letter}")

students = {"Spongebob", "Patrick", "Squidward", "Sandy", "Mr. Krabs"}
student = input("Enter a name of the student: ")
if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} is not a student")

grades = {"Sany": "A",
          "Squidward": "B",
          "Patrick": "C",
          "Mr. Krabs": "A"}
student = input("Enter a name of the student: ")
if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} is not a student")
    """
email = input("Enter your email: ")
if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")

