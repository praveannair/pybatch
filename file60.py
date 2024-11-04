import pandas as pd
score = [20,27,32]
# series = pd.Series(score)
series = pd.Series(score, index=["John","Cathy","Ria"])
# print(series) #try series[0] / series['John']
print(series['John'])

