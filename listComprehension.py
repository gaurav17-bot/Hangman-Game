doubles=[x*3 for x in range(1,11)]
print(doubles)

square=[y*y for y in range(1,11)]
print(square)

#
fruits=["Orange","apple","banana"]
fruits=[fruit.upper() for fruit in fruits]
for fruit in fruits:
    print(fruit)

#
numbers=[1,2,3,-4,5,-3]
positive=[x for x in numbers if x>=0]
print(positive)

#
even=[x for x in range(1,11) if x%2==0]
print(even)

#
grades=[]
