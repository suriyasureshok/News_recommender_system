import requests

API = '3a029167e178b9fdba7a4c5e749c7aff'
url = f'https://gnews.io/api/v4/top-headlines?lang=en&token={API}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for article in data.get('articles',[]):
        print(f"Title: {article['title']}")
        print(f"Description: {article['description']}\n")
else:
    print('Failed to retrieve data')