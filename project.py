import pandas as pd 

df=pd.read_csv('query.csv')
#print(df)


df[['Date', 'Time']] = df['time'].str.split('T', expand=True)  
df['time'] = df['Time'].str.split('.', expand=True)[0]  
df.to_csv('querys_with_split_columns.csv', index=False)

df.drop('time', axis=1, inplace=True)
print(df.head())    




