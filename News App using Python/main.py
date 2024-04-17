import requests
import json

query = input("What type of news are you interested in? " )
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-03-17&sortBy=publishedAt&apiKey=4b1c012db93a4b63bdf0d6b909abfb00"

r = requests.get(url)
news = json.loads(r.text)
# print(news, type(news))

for article in news["articles"]:
  print(article["title"])
  print(article["description"])
  print("-----------------------------")