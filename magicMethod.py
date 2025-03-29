class Student:
    def __init__(self,name,address,gpa):
        self.name=name
        self.address=address
        self.gpa=gpa
    
    def __str__(self):
        return f"Name: {self.name} \nAddress: {self.address}\nGPA: {self.gpa}"

std=Student("Gaurav Adhikari","Surkhet",3.70)
print(std)


############# comparing the objects of class using magic method ########################3
class area:
    def __init__(self,a):
        self.a=a
        
    def __gt__(self,other):      ## __gt__=='greater than' __lt__='less than' and __eq__ ='equal
        if self.a>other.a:
            return "First one is greater"
        else:
            return "Second is greater"
        
    def __add__(self,other):  ##magic method for adding
        return self.a+other.a
        
a1=area(10)
a2=area(12)
a3=area(123)
print(a1>a2)
print(a1+a2)

    