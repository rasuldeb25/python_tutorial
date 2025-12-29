#Match cases statement (switch) = an alternative to using many elif statements
#                                   execute some code if value matches a case
#                                   benefits: cleaner and syntax is more readable

"""
def day_of_week(day):
    match day:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            print("Invalid day")
day_of_week(2)


def is_weekend(day):
    match day:
        case "Sunday":
            return True
        case "Monday":
            return False
        case "Tuesday":
            return False
        case "Wednesday":
            return False
        case "Thursday":
            return False
        case "Friday":
            return False
        case "Saturday":
            return True
        case _:
            return False

print(is_weekend("Monday"))
"""

def is_weekend(day):
    match day:
        case "Sunday" | "Saturday":
            return True
        case "Monday"| "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return False

print(is_weekend("Sunday"))