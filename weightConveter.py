weight =float(input("Enter your weight: "))
unit=input("Kg or pounds:(K or P) ")
if unit=="K":
    weight= weight*2.205
    unit="pounds"
    print(f"Wright: {round(weight,2)}{unit}")
elif unit=="P": 
    weight=weight/2.205
    unit="kg"
    print(f"Weight: {round(weight,2)}{unit}")
else:
    print("Unit was not valid")

           