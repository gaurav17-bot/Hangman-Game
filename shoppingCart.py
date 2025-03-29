items=input("Enter the item that you are looking for: ")
price=float(input(f"Enter the price of the {items}: "))
quantity=int(input(f"Enter the quantity of the {items}: "))
total=price * quantity
print(f"Your total bill amount is ${total}")