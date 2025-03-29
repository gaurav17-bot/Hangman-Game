class Student:
    def __init__(self,m1,m2,m3):
        
        self.m1=m1
        self.m2=m2
        self.m3=m3
    
    def display(self):
        
        print(f"Marks 1: {self.m1}")
        print(f"Marks 2: {self.m2}")
        print(f"Marks 3: {self.m3}")

class detials(Student):
    def __init__(self,name,grade,address,gpa,m1,m2,m3):
         super().__init__(m1,m2,m3)
         self.name=name
         self.grade=grade
         self.address=address
         self.gpa=gpa
    
        
    def calcAverage(self):
       
        avg=(self.m1+self.m2+self.m3)/3
        print(f"Average: {avg}")
        
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Grade: {self.grade}")
        print(f"Address: {self.address}")
        print(f"GPA: {self.gpa}")
        super().display()
        

d=detials("Gaurav Adhikari","3rd sem","Surkhet",3.13,50,60,7)
d.display()
d.calcAverage()



    