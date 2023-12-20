import os
os.system("cls")

from datetime import datetime

my_date = "2023-12-22"
specified_date = datetime.strptime(my_date, "%Y-%m-%d")
today_date = datetime.now()
days_diff = (today_date - specified_date).days
print(days_diff)

def fun():
    return [1,3], [2,4]

x = fun()
a, b = x
print(a)
print(b)
