
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Titanic Dataset EDA Examples (Q81-Q100)

df=sns.load_dataset('titanic')

print(df.info())
print(df.describe())
print(df.isnull().sum())

df['age'].hist()
plt.show()

sns.countplot(x='class',data=df)
plt.show()

df['survived'].value_counts().plot.pie(autopct='%1.1f%%')
plt.show()

sns.boxplot(y='fare',data=df)
plt.show()

sns.scatterplot(x='age',y='fare',data=df)
plt.show()

corr=df.corr(numeric_only=True)
sns.heatmap(corr,annot=True)
plt.show()

print(df.groupby('sex')['survived'].mean())
