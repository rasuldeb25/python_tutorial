#indexing = accessing elements of square using [] (indexing operator)
#           [start:stop:step]

creditNumber = input("Enter your credit card number: ")
#lastDigits = creditNumber[-4:]
reversedDigits = creditNumber[::-1]
if not creditNumber.isdigit():
    print("Credit card number should only contain digits.")
elif len(creditNumber) > 12:
    print("Credit card number should not exceed 12 digits.")
else:
    #print("Your credit card number is: XXXXXXXX" + lastDigits + ".")
    print("Your reversed credit card number is: " + reversedDigits + ".")

"""
print(creditNumber[0])
print(creditNumber[:4])
print(creditNumber[5:9])
print(creditNumber[-12])
print(creditNumber[::2])
"""