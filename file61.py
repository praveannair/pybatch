import pandas as pd
marks = {
    'John':20,
    'Cathy':34,
    'Mike':45
}

# print(marks)

mySeries = pd.Series(marks)
# print(mySeries)
# mySeries = pd.Series(marks,index=['John','Cathy'])
print(mySeries)


# mySeries = pd.Series