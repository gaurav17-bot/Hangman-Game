import random


def spin_row():
    symbol=["⭐","⚽","🏀","🏏","🏐"]

    return[random.choice(symbol) for _ in range(3)]

def print_row(row):
    print("-----------")
    print(" | ".join(row))
    print("-----------")

def get_payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=='⭐':
            return bet *3
        
        if row[0]=="⚽":
            return bet *4
        
        if row[0]=="🏀":
            return bet *5
        
        if row[0]=="🏏":
            return bet *10
        
        if row[0]=="🏐":
            return bet *20
    return 0

def main():
    balance=100
    print("-----------------------")
    print("-Welcome to slot game-")
    print("ITEMS:⭐ ⚽ 🏀 🏏 🏐")
    print("-----------------------")

    while balance>0:
        print(f"Current balance:${balance}")
        
        bet=input("Enter bet amount:$")

        if not bet.isdigit():
            print("Enter valid amount")
            continue
        bet=int(bet)
        if bet>balance:
            print("insufficent amount")
            continue
        if bet<=0:
            print("Bet must be more than zero(0)")
            continue

        balance-=bet
        row=spin_row()
        print("Spinning....\n")
        print_row(row)

        payout=get_payout(row,bet)

        if payout>0:
            print(f"You won ${payout}")
        else:
            print("You lost !")

        balance+=payout
        play_again=input("Do you want to play again: (y/n): ").lower()
        if not play_again=='y':
            break

    print(f"Game over,Your final balance is: ${balance}")


if __name__=='__main__':
    main()



        
        
