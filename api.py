import requests
import pandas as pd

# # response = requests.get('https://jsonplaceholder.typicode.com/posts')

# # # print(response.status_code)   # 200 = success
# # # print(response.headers)       # metadata about the response
# # data = response.json()        # parse JSON response body
# # # print(type(data))             # list or dict
# # # print(data[0])                # first record

# response = requests.get('https://jsonplaceholder.typicode.com/posts')
# data = response.json()

# df = pd.DataFrame(data)
# print(df.shape)
# print(df.head())
# # Get posts by a specific user
# response = requests.get(
#     'https://jsonplaceholder.typicode.com/posts',
#     params={'userId': 1}
# )
# data = response.json()
# print(len(data))  # how many posts for user 1?


# all_posts = []
# page = 1

# while True:
#     response = requests.get(
#         'https://jsonplaceholder.typicode.com/posts',
#         params={'_page': page, '_limit': 10}
#     )
#     data = response.json()

#     if not data:          # empty page = we're done
#         break

#     all_posts.extend(data)
#     page += 1

# print(f'Total posts collected: {len(all_posts)}')
# df = pd.DataFrame(all_posts)
# print(df.shape)


# Hit https://jsonplaceholder.typicode.com/posts and load the response into a DataFrame. Print the shape and the first 3 rows.

response = requests.get('https://jsonplaceholder.typicode.com/posts')
data = response.json()
df = pd.DataFrame(data)
print(df.shape)
print(df.head(3))


# Use query params to fetch only posts where userId=3. How many posts does user 3 have?
# Hit https://jsonplaceholder.typicode.com/users and load it into a DataFrame. Print the column names — what data is available?
# Stretch: Fetch all posts using pagination (_page and _limit=5). Collect all pages into one DataFrame and print the final shape.