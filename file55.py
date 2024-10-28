# score=[5,8,9,6,4,3]
# def f(x):
#     return x+5
# result = map(f,score)
# print(list(result))

# score=[5,8,9,6,4,3]
# def f(x):
#     return x>5
# result = filter(f,score)
# print(list(result))

from functools import reduce
score=[5,8,9,6,4,3]
def f(x,y):
    return x+y
result = reduce(f,score)
print(result)

# def f(x):
#     return x*x

# sqr = map(f, [2,3,5,6])
# print(list(sqr))

# print(type(sqr))


