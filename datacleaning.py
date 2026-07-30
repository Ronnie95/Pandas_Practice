import pandas as pd



df = pd.DataFrame({
    'order_id': [1, 2, 2, 3, 4, 5],
    'customer': ['  DaRon', 'maya', 'maya', 'JAMES', 'Sofia', None],
    'total':    ['150.00', '89.99', '89.99', '-20.00', '300.00', '75.00'],
    'city':     ['Atlanta', 'chicago', None, 'Atlanta', 'MIAMI', 'Dallas']
})