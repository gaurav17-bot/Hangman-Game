class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

# car1.move()
collection=[car1,boat1,plane1]

for x in collection:
  x.move()

########################### Class Shape #################################################


class circle:
  def __init__(self,radius):
    self.radius=radius
    

  def area(self):
    a=3.14*self.radius*self.radius
    print(f"Area of circle: {a}")

class rectangle:
  def __init__(self,length,breadth):
    self.length=length
    self.breadth=breadth
  
  def area(self):
    a=self.length*self.breadth
    print(f"Area of rectangle :{a}")

c=circle(7)
r=rectangle(5,7)
for x in (c,r):
  x.area()

################ polymorphism in inheritance ############################################
import math

# Base class
class Shape:
    def area(self):
        return "Area method not defined"

# Derived class for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Derived class for Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Derived class for Triangle
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Function to demonstrate polymorphism
def print_area(shape):
    print(f"Area: {shape.area()}")

# Creating objects
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

# Calling function with different shapes
print_area(circle)     # Output: Area: 78.5398...
print_area(rectangle)  # Output: Area: 24
print_area(triangle)   # Output: Area: 12



