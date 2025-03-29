menu=({"pizza":3,"burger":2.4,"chowmin":1.3,"fry":4.8,"french":3.2})
print("--------------")
print("     MENU     ")
print("--------------")
cart=[]
total=0

for food,price in menu.items():
    print(f"{food:10}: ${price:.2f}")


while True:
    food=input("Enter any food to buy & (q) to quit: ").lower()
    if food=="q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
    # elif menu.get(food) is None:
        print("Food is not in MENU")
print("-----YOUR ORDER------")

for food in cart:
    total=total+menu[food] #menu[food]or menu.get(food)
    print(food,end=" ")
print()
print(f"Total is: {total:.2f}")



