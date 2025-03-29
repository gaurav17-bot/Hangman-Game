operator=input("Enter any operator(+ - * /)")
num1=int(input("Enter first num: "))
num2=int(input("Enter second number: "))
if operator =="+":
    result=num1+num2
    print(f"Result: {result}")
elif operator == "-":
    result=num1-num2
    print(f"Result: {result}")
elif operator =="*":
    result=num1*num2
    print(f"Result: {result}")
elif operator =="/":
    result=num1/num2
    print(f"Result: {result}")
else:
    print("Invalid choice")    