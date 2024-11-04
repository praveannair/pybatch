import pandas as pd
ds = {
    'name':['John','Cathy','Mike'],
    'age':[34,44,30],
}

# d = pd.DataFrame(ds)
d = pd.DataFrame(ds,index=['Rank1','Rank2','Rank3'])
# print(d)
# d.to_csv('test.csv')
print(d.loc['Rank1'])
