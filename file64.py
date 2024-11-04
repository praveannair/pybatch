import pandas as pd 
d= pd.read_csv('d:\\batches\\1800\\pybatch\\test.csv',header=None)
# d= pd.read_csv('d:\\batches\\1800\\pybatch\\test.csv',nrows=2,usecols=['name'])
print(d)