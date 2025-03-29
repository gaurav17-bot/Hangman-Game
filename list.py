# list=["apple","Banana","orange"]
# print(list[0])

# list=["apple","banana","orange"]
# for x in list:
#     print(x)

# fruit=["apple","Banana","orange","b"]
# print(len(fruit)) #length in string
# fruit[0]="a" #modification in list
# for x in fruit:
#     print(x)

# #append
# list=["a","b","c","d"]
# list.append("e")
# print(list) 

# #sort
# list=[4,5,6,35,66,78,53,2,123,34]
# list.sort()
# print(list)

#reverse
# list=[2,3,4,53,21,2,4,5,6,55]
# list.reverse()
# print(list)
# print(len(list))

#wap to enter nnumber of items in a list
# num=int(input("Enter the capacity of list: "))
# list=[]

# for i in range(1,num+1):
#     n=int(input(f"Enter {num} elements:  "))
#     list.append(n)
# print(f"Given list: {list} ")


array=[1,2,3,4,5]
even=[]
odd=[]
for x in array:
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)
print(f"Evens: {even}")
print(f"Odds: {odd}")


    
