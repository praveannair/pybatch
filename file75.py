import sys

fruits = ['apple','mango','cherry']
print(sys.getsizeof(fruits),"bytes")

myiterator = iter(fruits)
print(sys.getsizeof(myiterator),"bytes")

