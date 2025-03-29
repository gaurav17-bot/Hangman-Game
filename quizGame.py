questions=("What is your name?: ",
           "What is your fav food?: ",
           "Where do you live?: ",
           "Are you happy?: ")
options=(("A.Gaurav","B.Hari","C.Ram","D.Shyam"),
         ("A.Bhat","B.Dal","C.Roti","D.Tarkari"),
         ("A.Dailekh","B.Surkhet","C.Pokhara","D.Kathmandu"),
         ("A.Bit","B.No","C.Yes","D.Why?"))
answers=("A","D","B","C")
guesses=[]
score=0
question_nbr=0


for question in questions:
    print("................")
    print(question)
    for option in options[question_nbr]:
        print(option)
        

    guess=input("Enter your answer(A,B,C,D): ").upper()
    guesses.append(guess)
    if guess ==answers[question_nbr]:
        score+=1
        print("Correct!!")
    else:
        print("Incorrect!!")
        print(f"{answers[question_nbr]} is correct.")
        
    question_nbr+=1

print("**********")
print("  RESULT ")
print("**********")

print("Correct answers: ",end=" ")
for answer in answers:
    print(answer,end=" ")
print()

print("Your answers: ",end=" ")
for guess in guesses:
    print(guess,end=" ")
print()

score=int(score/len(questions)*100)
print(f"Your socre is : {score}%")

