import pandas as pd

s = pd.Series([1299.99, 89.99, 49.99], name='total')
print(s)

data = {
    'first_name': ['DaRon', 'Maya', 'James'],
    'city': ['Atlanta', 'Chicago', 'Atlanta'],
    'total_spent': [1389.98, 419.98, 49.99]
}

df = pd.DataFrame(data)
print(df)
print(df.shape)       # (rows, columns)
print(df.dtypes)      # data types per column
print(df.head(2))     # first 2 rows