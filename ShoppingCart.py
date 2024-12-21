# Shopping Cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (Q to quit): ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price of {food}: Rs."))
        foods.append[food]
        prices.append(price)

print("-----YOUR CART-----")
for food in foods:
    print(food, end = " ")

for price in prices:
    total = total + price

print(f"Your Total is: Rs.{total}")