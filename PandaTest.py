import pandas as pd
data=pd.read_csv("data/csvdata.csv",header=None,names=["c1","c2","c3","c4","c5","c6"],index_col=["c2","c3"])
print(data)
print(data.shape)
print(type(data))
print(data.head(2))
print(data.tail(2))
print(data.dtypes)
print(data["c1"])
print(type(data["c1"]))
#print(data[["c1"]])
#print(type(data[["c1"]]))
#print(list(data["c1"]))
#print((data[["c1","c2"]]))