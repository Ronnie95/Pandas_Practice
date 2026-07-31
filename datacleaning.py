import pandas as pd



df = pd.DataFrame({
    'order_id': [1, 2, 2, 3, 4, 5],
    'customer': ['  DaRon', 'maya', 'maya', 'JAMES', 'Sofia', None],
    'total':    ['150.00', '89.99', '89.99', '-20.00', '300.00', '75.00'],
    'city':     ['Atlanta', 'chicago', None, 'Atlanta', 'MIAMI', 'Dallas']
})

# Print the null count per column before cleaning.
print(df.isnull().sum())      # count nulls per column

# Fix the total column — cast to float, then remove any rows where total is negative or zero.

df['total']    = df['total'].astype(float)
df = df[df['total'] > 0]

# Standardize customer and city to Title Case with no leading/trailing spaces.

df['customer'] = df['customer'].str.strip().str.title()
df['city'] = df['city'].str.strip().str.title()

# Remove duplicate rows.
df = df.drop_duplicates()           # remove them

# Fill the null customer with 'Unknown' and null city with 'Unknown'.
df['customer'] = df['customer'].fillna('Unknown')
df['city'] = df['city'].fillna('Unknown')

# Add four assert statements to validate: no nulls in order_id, all totals positive, no duplicate order_ids, and both customer and city columns exist.
# # No nulls in critical columns
# assert df['order_id'].isnull().sum() == 0, "order_id has nulls"

# # All totals are positive
# assert (df['total'] > 0).all(), "Found negative or zero totals"

# # No duplicates
# assert df['order_id'].duplicated().sum() == 0, "Duplicate order IDs found"

# # Expected columns exist
# expected_cols = ['order_id', 'total', 'customer', 'city']
# assert all(col in df.columns for col in expected_cols), "Missing columns"

df = pd.DataFrame({
    'order_id': [1, 2, 2, 3, 4, 5],
    'customer': ['  DaRon', 'maya', 'maya', 'JAMES', 'Sofia', None],
    'total':    ['150.00', '89.99', '89.99', '-20.00', '300.00', '75.00'],
    'city':     ['Atlanta', 'chicago', None, 'Atlanta', 'MIAMI', 'Dallas']
})

print(df.isnull().sum())

df['total'] = df['total'].astype(float)
df = df[df['total'] > 0]

df['customer'] = df['customer'].str.strip().str.title()
df['city'] = df['city'].str.strip().str.title()

# Fill nulls FIRST so duplicates match properly
df['customer'] = df['customer'].fillna('Unknown')
df['city'] = df['city'].fillna('Unknown')

# Now drop duplicates — rows are fully comparable
df = df.drop_duplicates(subset=['order_id'], keep='first')
assert df['order_id'].isnull().sum() == 0, "order_id has nulls"
assert (df['total'] > 0).all(), "Found negative or zero totals"
assert df['order_id'].duplicated().sum() == 0, "Duplicate order IDs found"
assert all(col in df.columns for col in ['order_id', 'total', 'customer', 'city']), "Missing columns"

print(df)