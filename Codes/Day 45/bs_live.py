from bs4 import BeautifulSoup
import requests

responce = requests.get("https://appbrewery.github.io/news.ycombinator.com/")

yc_webpage = responce.text

soup = BeautifulSoup(yc_webpage, "html.parser")

articles = soup.find_all(name="a", class_ = "storylink")

article_text = []
article_link = []

for article_tag in articles:
    text = article_tag.getText()
    article_text.append(text)
    link = article_tag.get("href")
    article_link.append(link)
    
article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score" )]


# largest_number = max(article_upvote)
# lar_num_index = article_upvote.index(largest_number)

lar_num_index = article_upvote.index(max(article_upvote))

print(article_text[lar_num_index])
print(article_link[lar_num_index])
print(article_upvote[lar_num_index])