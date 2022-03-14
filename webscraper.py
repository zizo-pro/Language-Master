from bs4 import BeautifulSoup
from requests import get
from itertools import zip_longest

typ = input("ADJ or N").upper()
wrd = input("please enter a word: ")

if typ == "N":
	website = f"https://www.verbformen.com/declension/nouns/?w={wrd}"

elif typ == "T":
	website = f"https://www.verbformen.com/declension/adjectives/{wrd}.htm"

result = get(website)


src = result.content

soup = BeautifulSoup(src,"lxml")
# print(soup)

noun = soup.find("b").text

article = soup.find("p",{"class":"vGrnd rCntr"}).text
print(noun)
print(article[2:].replace("\n",""))

meaning = soup.find("p",{"class":"r1Zeile rU3px rO0px"})
word = meaning.text[3:-1]
print(word)

plural = soup.find("p",{"class":"vStm rCntr"}).text[1:]
print(plural.replace("\n·",""))

tye = soup.find("p",{"class","rInf"})
print(tye.find(attrs={"title":["noun","adjective"]}).text)


