import datetime

date=datetime.date(2025,3,4) #to set the date
today=datetime.date.today() ## to get the real date
print(today)

####### formating date and time and also getting current date and time

import datetime
time=datetime.datetime.now()
time=time.strftime("%H:%M:%S  %d/%m/%Y")
print(time)