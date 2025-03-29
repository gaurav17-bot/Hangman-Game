class Animal:
    count=0
    def __init__(self,name,type,habitat):
        self.name=name
        self.type=type
        self.habitat=habitat
        count=+1
    
    def display(self):
        print(f"Hello {self.name}")
        print(f"Are you {self.type}")
        print(f"Do you live in {self.habitat}")

class dog(Animal):
    pass
class cat(Animal):
    pass

d=dog("German","Domestic animal","house")
c=cat("Mewo","wild","Jungle")
d.display()
c.display()
print(f"Count {Animal.count}")