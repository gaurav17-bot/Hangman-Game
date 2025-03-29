# name=input("Enter your name: ")
# while name=="":
#     print("you didnot entered ")
#     name=input("Enter your name")
# print(f"Hello {name}")    

age=int(input("Enter your age: "))
while age<=0:
    print("Age cant be negative or zero")
    age=int(input("Enter your age: "))
print(f"Ohh you are {age} years old")    
