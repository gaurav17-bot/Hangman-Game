# *args
# **kwargs


# *args
def add(*args):
    sum=0
    # print(type(args)) this is class type
    for arg in args:
        sum=sum+arg
    return sum

result=add(2,6,10,20)
print(f"Sum: {result}")


# **kwargs

def student(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
    
d=student(name="Gaurav ad",id="1",grade="bachlor")


