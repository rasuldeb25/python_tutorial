import random

# ● ┌ ─ ┐ │ └ ┘

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│         │",
        "│    ●    │",
        "│         │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│         │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│    ●    │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│         │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│    ●    │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘")
}
dice =[]
total = 0
number_of_dice = int(input("How many dice?: "))
for die in range(number_of_dice):
    dice.append(random.randint(1,6))

for line_num in range(len(dice_art[1])):
    for die_value in dice:
        print(dice_art[die_value][line_num], end="  ")
    print()


for die in dice:
    total+= die
print(f"Total is: {total}")