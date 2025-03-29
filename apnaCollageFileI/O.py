##reading a file#####

f=open("C:/Users/Lenovo/OneDrive/Desktop/python self/apnaCollageFileI/gaurav.txt", "r")

data=f.read() ##reading whole file at atime
print(data)

a=f.readline() ##reading file line by line
print(a)
b=f.readline()
print(b)
f.close()


##### write a file #############
f=open("C:/Users/Lenovo/OneDrive/Desktop/python self/apnaCollageFileI/gaurav.txt", "w")
f.write("Hello i am learning python")

f=open("C:/Users/Lenovo/OneDrive/Desktop/python self/apnaCollageFileI/gaurav.txt", "a")
# 'a' appends the new written data with existing data where 'w' replaces old data
f.write("\nI am gaurav adhikari")

# it automatically create a file after writing "a" or "w" 
f=open("sample.txt","a")
f.write("\nAre you learning python")
f.close()

f=open("sample.txt","r") #reading the same file
print(f.read())


####### reading and writing at same time using "r+"
f=open("new.txt","a+")
f.write("Hello you are reading\nand writing a file")
d=f.read()
print(d)
f.close


##### using with syntax ######
with open("new.txt","r") as f:
    data=f.read()
    print(data)



########## Some practice of file i/o

f=open("hello.txt","w")
f.write("Hello gaurav\ndo you have been to kathmandu")

####### to modify some word in a file#############
f=open("hello.txt","r")
data=f.read()
modifide=data.replace("kathmandu","Surkhet")
print(modifide)

f=open("hello.txt","w")
f.write(modifide)
f.close()


########## to serach the word exists in file or not##########
f=open("hello.txt","r")
d=f.read()
print(d)
if ("Surkhet" in d):
    print("found")
else:
    print("Not found")

### checking thw word is in which line

def check_for_line():
    word="are"
    data=True
    line_no=1
    with open("hello.txt","r") as f:
        while data:
            data=f.read()
            if(word in data):
                print(line_no)
                return
            line_no=line_no+1
    return -1

print(check_for_line())
    


        