acc_number="0234-345A-5324"
password=1064
amount=1000
while True:
    number=input("Account Number: ")
    if number==acc_number:
        pin=int(input("Password: "))
        if pin==password:
            while True:
                print("\n---OUR SERVICES---")
                print("1.Deposit\n2.Withdraw\n3.Enquiry\n4.Exit")
                ch=input("Enter your choice: ")
                if not ch.isdigit():
                    print("Please enter digits(1-4) ")
                    continue
                ch=int(ch)
                match ch:
                    case 1:
                        dep_amt=int(input("Enter amount: "))
                        amount=amount+dep_amt
                    case 2:
                        draw=int(input("Enter amount: "))
                        if amount<draw or amount<=1000:
                            print("Insufficient balance")
                        else:
                            amount=amount-draw
                    case 3:
                        print(f"Total amount: {amount}")
                    case 4:
                        exit(0)
                    case _:
                        print("Invalid choice(1-4)")
        else:
            print("Incorrect password")
    else:
        print("Incorrect Account Number")


