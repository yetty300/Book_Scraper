import requests
from bs4 import BeautifulSoup

# get url to scrape and use get to retrieve html code from product on site
url = "http://books.toscrape.com/catalogue/sorting-the-beef-from-the-bull-the-science-of-food-fraud-forensics_736/index.html"
page = requests.get(url)


print(page.content)
#
soup = BeautifulSoup(page.content, "html.parser")

for link in soup.find_all('a'):
    print(link.get('href'))
#url = soup.find_all('a', href_="../category/books_1/index.html")
#print (url)


upc = soup.table.td
print(upc.string)

title = soup.title.string
print(title)

priceWithTax = soup.price
print(priceWithTax)

priceNoTax = soup.price
print(priceNoTax)

quantity = soup.Availability
print(quantity)

sample = ''
description = soup.find_all(class_="sub-header")
print(description)

sample = '<a href="../category/books/science_22/index.html">Science</a>"'
soup = BeautifulSoup(sample, "html.parser")
print(soup.get_text())
#print(category)

review = soup.review
print(review)

sample = ""
soup = BeautifulSoup(sample, "html.parser")
image = soup.image