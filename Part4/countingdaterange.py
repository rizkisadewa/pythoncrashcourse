# Couting Date Range
import datetime

def balance(date1, date2):
    result = abs(date1 - date2)
    return result.days

date1 = datetime.date(2019, 10, 14)
date2 = datetime.date(2019, 10, 18)

print("Date Range between %s and %s is = " % (date1, date2))
print(balance(date1, date2),' nights')
