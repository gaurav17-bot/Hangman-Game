import random
options=["Paper","Scissor","Rock"]
playing=True
while playing:
    player=None
    CPU=random.choice(options)

    while player not in options:
        player=input("Enter your choice(Rock,Paper,Scissor): ")
    print(f"Player: {player}")
    print(f"Computer: {CPU}")

    if player==CPU:
        print("Its a tie!")
    elif player=="Scissor" and CPU=="Paper" or player=="Rock" and CPU=="Scissor" or player=="Paper" and CPU=="Rock":
        print("Player wins")
    else:
        print("Computer wins") 

    if not input("Play again?(y/n): ").lower()=="y":
        playing=False
print("Thankyou for palying")   
