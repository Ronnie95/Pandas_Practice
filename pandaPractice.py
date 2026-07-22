import pandas as pd

# s = pd.Series([1299.99, 89.99, 49.99], name='total')
# print(s)

# data = {
#     'first_name': ['DaRon', 'Maya', 'James'],
#     'city': ['Atlanta', 'Chicago', 'Atlanta'],
#     'total_spent': [1389.98, 419.98, 49.99]
# }

# df = pd.DataFrame(data)
# print(df)
# print(df.shape)       # (rows, columns)
# print(df.dtypes)      # data types per column
# print(df.head(2))     # first 2 rows


# Read a CSV
# df = pd.read_csv('orders.csv')

# # Read JSON
# df = pd.read_json('orders.json')

# # First look at any dataset
# print(df.shape)
# print(df.head())
# print(df.info())       # column names, types, null counts
# print(df.describe())   # statistics for numeric columns

# 1. Create a DataFrame with at least 5 rows representing orders — columns: order_id, customer_name, product, total, city. Print the shape, dtypes, and first 3 rows.
data = {
    'order_id': [1,2,3,4,5],
    'first_name': ['Rob', 'Ron', 'Bud', 'Tyler', 'Pal'],
    'product': ['Bike', 'Scooter', 'Skates', 'Rollers', 'Skate Board'],
    'total': [100,200,340,440,554],
    'city': ['Atlanta', 'Baltimore', 'New York', 'Los Angeles', 'Miami']
}

df = pd.DataFrame(data)
# print(df.shape)
# print(df.info()) 


# 2. Filter the DataFrame to show only orders where total is above 200. Print the result.

print(df[df['total'] > 200])

# 3. Add a new column called tax that is 8% of total. Print the updated DataFrame.
df['tax'] = df['total'] * 0.08

print(df)
# 4. Sort the DataFrame by total descending and print it.

# Sort by total in descending order
df_sorted = df.sort_values(by='total', ascending=False)

print(df_sorted)
