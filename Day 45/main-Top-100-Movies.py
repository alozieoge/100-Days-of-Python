from bs4 import BeautifulSoup
import requests
import lxml

# TOP_MOVIES_URL = "https://www.empireonline.com/movies/features/best-movies-2/" Not able to get movie tags
TOP_MOVIES_URL = "https://stacker.com/stories/1587/100-best-movies-all-time"


# Scrap top 100 movies data
response = requests.get(url=TOP_MOVIES_URL)
# print(response.text)
webpage_html = response.text

soup = BeautifulSoup(markup=webpage_html, parser="html.parser", features="lxml")
print(soup.prettify())

# Drill down to the tag which contains the movie number and name.
all_movies = soup.select(selector="div div div h2 div")
all_movies = all_movies[1:]
# print(all_movies)

movie_titles = []
for movie in all_movies:
    text = movie.getText()
    movie_titles.append(text[1:])

top_100_movies = movie_titles[::-1]
print(top_100_movies)

# Write data fo text file
with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in top_100_movies:
        file.write(f"{movie}\n")
