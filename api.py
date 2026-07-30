import requests
import pandas as pd

# response = requests.get('https://jsonplaceholder.typicode.com/posts')

# # print(response.status_code)   # 200 = success
# # print(response.headers)       # metadata about the response
# data = response.json()        # parse JSON response body
# # print(type(data))             # list or dict
# # print(data[0])                # first record

response = requests.get('https://jsonplaceholder.typicode.com/posts')
data = response.json()

df = pd.DataFrame(data)
print(df.shape)
print(df.head())
# Get posts by a specific user
response = requests.get(
    'https://jsonplaceholder.typicode.com/posts',
    params={'userId': 1}
)
data = response.json()
print(len(data))  # how many posts for user 1?