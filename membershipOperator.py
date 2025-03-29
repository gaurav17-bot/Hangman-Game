name="Gaurav Adhikari"
letter=input("Enter any letter: ")
if letter in name:
    print("Letter is in word")
else:
    print("Letter not in word")

#
grades={"Gaurav":"A","Deepak":"B","Sharban":"C"}
student=input("Enter the name of student: ")
if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")

#
email=input("Enter your email: ")
while True:
    if "@" not in email and "." not in email:
        print("Invalid email")
        email=input("Enter your email: ")

        
    else:
       password=input("Enter password: ")
       print("Welcome")
       break