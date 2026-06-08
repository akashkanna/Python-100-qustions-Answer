
import pandas as pd

# Q61
s=pd.Series([10,20,30])

# Q62
df=pd.DataFrame({'Name':['A','B'],'Age':[20,25]})

# Q63-Q66
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)

# Q67-Q80 examples
print(df['Age'])
df['Salary']=[1000,2000]
df.rename(columns={'Age':'Years'},inplace=True)
print(df.isnull().sum())
