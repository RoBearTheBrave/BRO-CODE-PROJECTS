#create a program that simulates rolling dice by creating an output that looks like dice

import random

#use unicode to create the symbols needed for the dice
#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518") 

# output is: ● ┌ ─ ┐ │ └ ┘
#use this to create ascii art that will make the dice

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dice_art = {
    1: ("┌───────┐",
        "│       │",
        "│   ●   │",
        "│       │",
        "└───────┘"),
    2: ("┌───────┐",
        "│ ●     │",
        "│       │",
        "│     ● │",
        "└───────┘"),
    3: ("┌───────┐",
        "│ ●     │",
        "│   ●   │",
        "│     ● │",
        "└───────┘"),
    4: ("┌───────┐",
        "│ ●   ● │",
        "│       │",
        "│ ●   ● │",
        "└───────┘"),
    5: ("┌───────┐",
        "│ ●   ● │",
        "│   ●   │",
        "│ ●   ● │",
        "└───────┘"),
    6: ("┌───────┐",
        "│ ●   ● │",
        "│ ●   ● │",
        "│ ●   ● │",
        "└───────┘")
}


dice = []
total = 0
number_of_dice = int(input("Enter the number of dice to roll: "))

for i in range(number_of_dice):
    dice.append(random.randint(1, 6))

#display the ascii art for each die rolled
#this loop will print the dice in a vertical line
# for die in dice:
#     for line in dice_art.get(die):
#         print(line)

#create a horizontal line of dice
for line in range(5): #loop through each line of the dice to print them side by side
    for die in dice:
        print(dice_art.get(die)[line], end = " ")
    print()


for die in dice:
    total += die
print(f"Total: {total}")
 