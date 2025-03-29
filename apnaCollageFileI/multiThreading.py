import threading

def find_cube(num):
    cube=num*num*num
    print(f"Cube of {num} is {cube}")

def find_square(num):
    square=num*num
    print(f"Square if {num} is {square}")
    
   
if __name__=="__main__":
    t1=threading.Thread(target=find_cube,args=(10,))
    t2=threading.Thread(target=find_square,args=(5,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("Done!")




####### OR #######(same)


import threading


def print_cube(num):
    print("Cube: {}" .format(num * num * num))


def print_square(num):
    print("Square: {}" .format(num * num))


if __name__ =="__main__":
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done!")
