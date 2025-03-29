username=input("username: ")
if len(username)>12:
    print("Your user name cant contain more than 12 letters")

elif not username.find(" ")== -1:
    print("Your user name cant contains space")

elif not username.isalpha():
    print("Cant contain digits")

else:
    print(f"Welcome {username}")    