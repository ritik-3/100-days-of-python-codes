from bs4 import BeautifulSoup 
import lxml

with open("Codes/Day 45/website.html") as file:
    CONTENT = file.read()
    
soup = BeautifulSoup(CONTENT,"html.parser")
print(soup.title)
print(soup.title.string)
print(soup.prettify())