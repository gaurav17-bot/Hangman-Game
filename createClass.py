######class student
class student:
    
    def  __init__(self,name,m1,m2,m3):
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def findavg(self):
        avg=(self.m1+self.m2+self.m3)/3
        return avg
    
    def display(self):
        print(f"Name: {self.name}")

s=student("Gaurav Adhikari",50,60,70)
s.display()
a=s.findavg()
print(f"Average: {a}")

##############class car
class car:
    car_count=0
    def __init__(self,name,brand,year,forSale):
        self.name=name
        self.brand=brand
        self.year=year
        self.forSale=forSale
        car.car_count+=1 #using actual class name instead of its object
    
    def display(self):
        print(f"Name of car: {self.name}")
        print(f"Brand: {self.brand}")
        print(f"Year: {self.year}")
        print(f"Is car in sell: {self.forSale}")

c=car("Mustang","Toyata",2024,False)
c1=car("Nano","Tata",2005,True)
print("Car1 details: ")
c.display()
print("\nCar2 details: ")
c1.display()
print(f"Numbers of cars: {car.car_count}")#we usually call class variable with class name 