foods=[]
prices=[]
total=0

while True:
    food=input("Enter the food you wanted to buy: ")
    if food=="q":
        break
    else:
        price=float(input(f"Enter the pirce of {food}: $"))
        foods.append(food)
        prices.append(price)
print("****YOUR CART****")
for food in foods:
    print(food)
for price in prices:
    total+=price
print(f"Total amount: ${total}")

