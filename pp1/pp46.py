#exception = an event that interrupts the flow of the program
#           (ZeroDivisionError, TypeError, ValueError)
#           1. try 2. except 3. finally
try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("You can enter only numbers!")
except Exception:
    print("Something went wrong!")
finally:
    print("Do some clean up here!")