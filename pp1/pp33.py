#if__name__==main__ = (this script can be imported or run standalone)
#                       functions and classes in this module can be reused
#                       without them main block of code being executed

def fav_food(food):
    print(f"My favorite food is {food}")

def main():
    print("This is the main function")
    fav_food("Pizza")
    print("goodbye")
print(__name__)
if __name__ == '__main__':
    main()