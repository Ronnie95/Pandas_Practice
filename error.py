records = [
    {'order_id': 1, 'total': '150.00'},
    {'order_id': 2, 'total': 'INVALID'},
    {'order_id': 3, 'total': '89.99'},
    {'order_id': 4, 'total': '-50.00'},
    {'order_id': 5, 'total': '300.00'},
]

def safe_cast_records(records):
    good_records = []
    bad_records = []

    for record in records:
        new_record = record.copy()
        try:
            new_record['total'] = float(new_record['total'])
            if new_record['total'] <= 0:
                new_record['_error'] = "total must be positive"
                bad_records.append(new_record)
            else:
                good_records.append(new_record)
        except ValueError:
            new_record['_error'] = "cannot cast total to float"
            bad_records.append(new_record)

    return good_records, bad_records

good, bad = safe_cast_records(records)

import pandas as pd
print("GOOD:")
print(pd.DataFrame(good))
print("\nBAD:")
print(pd.DataFrame(bad))