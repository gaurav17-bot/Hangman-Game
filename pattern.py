num=int(input("Enter a number: "))
for x in range(0,num+1):
    for y in range(0,x):
        print("*",end="")
    print()