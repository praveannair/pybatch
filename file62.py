import pandas as pd
marks = {
    'John':[20,56],
    'Cathy':[34,44],
    'Mike':[45,34]
}
# myseries = pd.DataFrame(marks)
# print(myseries)
myseries = pd.DataFrame(marks,index=['Maths','Science'])
# print(myseries)
print(myseries['Cathy'])
