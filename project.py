import pandas as pd 
df=pd.read_csv('query.csv')
print(df)

headers = df.columns.tolist()
print(headers)


