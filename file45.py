# import datetime as d
# print(d.date.today())
# print(d.date.today().year)
# print(d.date.today().month)
# print(d.date.today().day)
# print(d.date.today().weekday()) #monday is 0

# import time as t
# print("Before")
# t.sleep(3)
# print("After")

# import random as r
# print(r.randint(3, 9))

# mylist = ["apple", "banana", "cherry"]
# fruit = r.choice(mylist)
# print(fruit)
# print(r.choice(mylist))

import random as r
print("** Math Quiz ***")
i=1
while i<=5:
    a = r.randint(1,9)
    b = r.randint(1,9)
    print(f"{i}.{a}+{b}=")
    i=i+1






