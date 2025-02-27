import pandas as pd
df = pd.read_csv('query.csv')
df['time'] = pd.to_datetime(df['time'])

df['Date'] = df['time'].dt.strftime('%d-%m-%Y')
df['Time'] = df['time'].dt.strftime('%H:%M:%S')

df.drop('time',axis=1, inplace=True)
df = pd.concat([df.iloc[:, -2:], df.iloc[:, :-2]], axis=1)
df.to_csv('final_querys.csv', index=False)
print(df.head())