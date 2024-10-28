# upper = lambda str: str.upper()
# print(upper("hello"))

# sqr = lambda x:x*x
# print(sqr(5))

# add = lambda x,y:x+y
# print(add(4,5))

# greater = lambda x,y:x if x>y else y
# print(greater(4,5))

num = [5,6,4,3]
numList = lambda x:(i for i in x if i>4)
print(list(numList(num)))