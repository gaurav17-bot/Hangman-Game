# import time
# my_time=int(input("Enter time in seconds: "))

# for x in range(0,my_time):
#     print(x)
#     time.sleep(1)
# print("Time up!")

# import time
# my_time=int(input("Set timer (in seconds) : "))
# for x in reversed(range(1,my_time)):
#                   print(x)
#                   time.sleep(1)
# print("Happy New Year!!!")

#DIGITAL CLOCK

import time
myTime=int(input("Enter time in seconds: "))
for x in range(myTime,0,-1): # -1 counts as reverse like 123 in 321
    seconds=x%60
    minutes=int(x/60)%60
    hours=int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
