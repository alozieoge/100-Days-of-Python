from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
# print(response.text)
yc_web_page = response.text

soup = BeautifulSoup(markup=yc_web_page, parser="html.parser", features="lxml")
# print(soup.prettify())

# To get the webpage title
# print(soup.title)

# To get the tag of the 1st article on the webpage - text, link and score
article_tag = soup.find(name="a", class_="storylink")
# print(article_tag)
article_text = article_tag.getText()
article_link = article_tag.get("href")
article_upvote = soup.find(name="span", class_="score").getText()

# print(article_text)
# print(article_link)
# print(article_upvote)

# To get all occurrences of the articles on the webpage
article_tags = soup.find_all(name="a", class_="storylink")
all_upvotes = soup.find_all(name="span", class_="score")

article_texts = []
article_links = []
for article_tag in article_tags:
    article_texts.append(article_tag.getText())
    article_links.append(article_tag.get("href"))

article_upvotes = [int(score.getText().split()[0]) for score in all_upvotes]

print(article_texts)
print(article_links)
print(article_upvotes)

# Print out the article title and link with the highest number of upvotes.
max_upvote = max(article_upvotes)
id_max_upvote = article_upvotes.index(max_upvote)
print(id_max_upvote, max_upvote)

print(article_texts[id_max_upvote])
print(article_links[id_max_upvote])
print(article_upvotes[id_max_upvote])
