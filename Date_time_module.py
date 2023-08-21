from datetime import *


#finding current data and time
now = datetime.now()
print(now)
print(f"date now {now.day}/{now.month}/{now.year}")
print(f"Time now {now.hour}:{now.minute}:{now.second}")

#finding today's date and time
tdm =datetime.today()
print("Today's date and time= ", tdm)
td = date.today()
print("Today's date is : ", td)
#find the week day name

day = td.strftime("%A")
print("It is ", day)