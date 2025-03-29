import random


option=["Rock","Paper","Scissor"]

while True:
     
     user1=random.choice(option)
     You=input("Enter your choice: (Rock,Paper or Scissor: ) or q to quit: ").capitalize()
     if You=="Q":
         print("Thankyou for playing!!")
         break
     elif You not in option:
         print("Invalid choice")


     if user1=="Scissor" and You=="Paper" or user1=="Rock" and You=="Scissor" or user1=="Paper" and You=="Rock":
        print(f"User1 gets: {user1}")
        print(f"User2 gets: {You}")
        print("User 1 is winner")
     elif user1==You:
        print(f"User1 gets: {user1}")
        print(f"User2 gets: {You}")
        print("Equal")
     else :
        print(f"User1 gets: {user1}")
        print(f"User2 gets: {You}")
        print("User 2 is winner")
print("--------------------------")
     