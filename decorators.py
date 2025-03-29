def len(fun):
    def wrapper(*args,**kwargs):
        print("Area is: ")
        fun(*args,**kwargs)
    return wrapper

@len
def area(len):
    area=len*len
    print(area)

area(5)