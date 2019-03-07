# Date
import time
print(time.time())
print(time.localtime(time.time()))

print()

# show the date and time with format
print(time.strftime('%A, %d %B %Y %H:%M:%S', time.localtime(time.time())))

'''
Format=>Description=>Value
a=>Day Name (Abbrevation)=>depend on local
A=>Day Full Name => depend on local
b=>Month Name (Abbrevation) => depend on local
B=>Month Full Name => depend on local
c=>Full Reference of Time=> depend on local
d=>day number in one month=> 1..31
H=>Hour(24)=>0..23
h=>Hour(12)=>1..12
j=>day number in one year=>1..366
m=>month number in one year=>1..12
M=>minutes=>0..59
P=>A.M or P.M.=> depend on local
w=>day number in one week=> 0..6 (0 is Sunday)
x=>Full represent of Date=> depend on local
X=>Full represent of Time=> depend on local
Y=>year number in one century => 0..99
Z=>time local zone=>empty if not specified
'''

# Another example
print(time.strftime('%a, %d/%m/%Y %H:%M:%S', time.localtime(time.time())))

# datetime
import datetime
date = datetime.date.today()
print(date)
print(date.day)
print(date.month)
print(date.year)

now = datetime.datetime.now()
print(now)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)
print(type(now))
