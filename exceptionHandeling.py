try:
    number=int(input("Enter any number: "))
    ans=number*number
    print(f"Square of {number} is {ans}")

except ValueError:
    print("Enter only numbers please !")

except TypeError:
    print("Parameters should be of same type")
    
finally:
    print("Thanks for performing")  