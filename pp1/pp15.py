#for loops = execute a block of code a fixed number of times
#              You can iterate over a range, sting, sequence, etc

"""
#for x in  range(1, 11):
for x in reversed(range(1,11, 2)):
    print(x)
print("Happy new year!")
"""
for x in range(1,21):
    if x == 13:
        break            #continue
    else:
        print(x)