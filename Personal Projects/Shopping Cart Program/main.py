# Shopping Cart

# We will have 2 lists
# Use of lists because tuples are unchangeable, since the input from the user can not be appended into a tuple

foods = []
prices = []
total = 0

while True:
    food = input("Enter what food you would like to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print('----- YOUR CART -----')

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print()
print(f"Your total is: ${total}")