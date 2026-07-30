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
# Remove duplicate rows.
# Fill the null customer with 'Unknown' and null city with 'Unknown'.
# Add four assert statements to validate: no nulls in order_id, all totals positive, no duplicate order_ids, and both customer and city columns exist.