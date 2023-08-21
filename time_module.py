import time

epoch = time.time()
print(epoch)# 1970 to current time in second

t = time.localtime(epoch)
d = t.tm_mday
m = t.tm_mon
y = t.tm_year
print(f"current date is {d}\{m}\{y}")

h = t.tm_hour
m = t.tm_min
s = t.tm_sec
print(f"current time is {h}:{m}:{s}")
# finding current data and time using ctime()
t = time.ctime()
print(t)