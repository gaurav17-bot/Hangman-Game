day=int(input("Enter any number(1-7): "))
match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thuresday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("Invalid choice(1-7)")