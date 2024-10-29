from functools import reduce 

#map(function, iterable)

# def f1(x):
#     return x*2

# result = list(map(f1, [2,3,5,6]))
# print(result)

# squares_list = list(map(lambda n: n * 2, [2,3,5,6]))
# print(squares_list)

#filter(function, iterable)


even_num_list = list(filter(lambda n: n % 2 == 0, [2,3,5,6]))
print(even_num_list)

#reduce(function, iterable)
total = reduce(lambda x,y: x+y, [2,3,5,6])
print(total)

# list1 = [i if i % 2 == 0 else 0 for i in range(1, 11)]
# print(list1)

num = [i  if i>2 else 0 for i in range(5) ]
print(num)




