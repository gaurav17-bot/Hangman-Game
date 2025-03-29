class employee:
    def __init__(self,name,address):
        self.name=name
        self.address=address
    
    def diplay(self):
        print(f"{self.name} is {self.address}")
    
    @staticmethod
    def is_valid(position):
        valid_position=["Manager","MD","Receptionist"]
        if position in valid_position:
            print("Candidate is valid")
        else:
            print("Invalid candidate")

emp=employee("Gaurav Adhikari","Manager")
emp.diplay() #calling instance method by instance or object
employee.is_valid("Manager") #calling static method by class name and donot need access to class data




#####################
class area:
    @staticmethod
    def find_area(length,breadth):
        area=length*breadth
        print(f"Area :{area}")
    
area.find_area(2,4)