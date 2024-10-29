# from collections import Counter
# names=["john","cathy","john","ria","john"]
# mycounter = Counter(names)
# print(mycounter)
# print(mycounter.most_common(2))

# from collections import namedtuple
# Price = namedtuple('Price',['orange','mango','apple'])
# p = Price(23,43,47)
# print(p)
# print(p.orange)


# from collections import defaultdict
# d = defaultdict(int) #try float
# d['a']=34
# d['b']=45
# print(d['a'])
# print(d['r'])


# from collections import deque
# d=deque([3,5,1])
# d.append(6)
# d.appendleft(9)
# d.pop()
# d.popleft()
# d.clear()
# d.extend([4,5,7])
# d.extendleft([0,6,1])
# d.rotate(2)
# print(d)

# from collections import ChainMap
# d1 = {'a':3,'b':6}
# d2 = {'c':7,'d':8}
# d3 = ChainMap(d1,d2)
# # print(d3['a'])
# for i,j in d3.items():
#     print(i,j)


from collections import UserList

class MyList(UserList):
	def pop(self, s = None):
		raise RuntimeError("Deletion not allowed")


L = MyList([1, 2, 3, 4])

L.pop()
print(L)



