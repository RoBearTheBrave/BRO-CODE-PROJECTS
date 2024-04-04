# pratice data collections with a shopping cart

# we don't want to use a tuple because we want to be able to modify the list

foods = []
prices = []
total = 0

while True:
    food = input("Enter food to buy (q to quit): ").strip()
    if food.lower() == "q":
        print("Quitting...")
        break
    else:
        price = float(input(f"Enter price of {food}: $"))
        foods.append(food)
        prices.append(price)

print("----------YOUR CART----------")

for food in foods:
    print(food)

for price in prices:
    total += price
print()
print(f"Total: ${total:.2f}")