from bs4 import BeautifulSoup 
import lxml

with open("Codes/Day 45/website.html") as file:
    CONTENT = file.read()
    
soup = BeautifulSoup(CONTENT,"html.parser")
# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())

all_ancor = soup.find_all(name="a")

for tag in all_ancor:
    print(tag.getText())
    print(tag.get("href"))


heading = soup.find(name="h1", id="name")
print(heading)