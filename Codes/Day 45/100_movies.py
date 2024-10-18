from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

responce = requests.get(URL)
website_html = responce.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

movie_titles = [movies.getText() for movies in all_movies]
movies = movie_titles[::-1]

with open("Codes/Day 45/movies.text", mode="w") as file:
    for movie in movies:
        print(movie)
        file.write(f"{movie}\n")