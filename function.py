def findArea(r):
    area=3.14*r*r
    return area

radius=int(input("Enter radius: "))
area=findArea(radius)
print(f"Area of circle is: {area:.2f}")


def myFullname(first,last):
    first=first.capitalize()
    last=last.capitalize()
    return first+" "+last

name=myFullname("gaurav","adhikari")
print(name)


