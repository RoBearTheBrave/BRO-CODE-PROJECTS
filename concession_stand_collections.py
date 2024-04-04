#create a concession stand that sells food and drinks

#use a dictionary to store the items and their prices

menu = {"hot dog": 3.50,
        "hamburger": 5.50,
        "fries": 2.50,
        "soda": 1.50,
        "water": 1.00,
        "popcorn": 6.00
        }

cart = []
total = 0

#the menu is a 2d collection, so we need to lay it down flat to print it out

print("------------MENU------------")
for key, value in menu.items():
    #format the data to make it look like a menu
    print(f"{key:10}: ${value:.2f}")
print("----------------------------")

while True:
    food = input("Enter an item from the menu or 'q' to quit: ").strip().lower()
    if food == "q":
        break
    elif menu.get(food) == None:
        print("Sorry, that item is not on the menu.")
    elif menu.get(food) != None:
        cart.append(food)

print("------------Your Order------------")
for food in cart:
    total += menu.get(food) #get the value of the food from the menu and add it to the total
    print(food, end = " ") #print the food on the same line with a space between them

print(f"\nYour total is: ${total:.2f}")
