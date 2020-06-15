import numpy as np
import pandas as pd
import seaborn as sns
from numpy.random import randn

df=pd.DataFrame(randn(1000),index=pd.date_range('2019-06-07',periods=1000),columns=["value"])
ds=pd.Series(randn(1000),index=pd.date_range('2019-06-07',periods=1000))
print(df)
print(ds)
print(df.plot())
