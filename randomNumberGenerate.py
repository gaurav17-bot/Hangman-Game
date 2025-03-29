import random
number=random.randint(1,15)


while True:
    guess=int(input("Enter yout guess: "))
    if guess==number:
        print("wow you guess exactly same !!")
        print(f"The random number is: {number}")
        print(f"Your guess is: {guess}")
        break
    elif guess==111:
        print("I gave up")
        break     
    elif guess>number:
        print("Guess some small numbers")
    else:
        print("Guess some largest number")
