import requests
import re
import csv
from bs4 import BeautifulSoup

# get url to scrape and use get to retrieve html code from product on site
url = "http://books.toscrape.com/catalogue/sorting-the-beef-from-the-bull-the-science-of-food-fraud-forensics_736/index.html"
page = requests.get(url)

# turn html into readable code
soup = BeautifulSoup(page.content, "html.parser")
#print(soup.prettify())

content = soup.find('ul', class_='breadcrumb')


url = "http://books.toscrape.com/catalogue/sorting-the-beef-from-the-bull-the-science-of-food-fraud-forensics_736/index.html"
print(url)

#Method 1 of getting UPC
UPC= soup.find('td').get_text()
print("The upc code of the book is: " + UPC)
#Method 2 of getting UPC
upc = soup.table.td
print("The upc code of the book is: " + upc.string)

title = soup.title.string
print("The title of the book is: " + title)

priceWithTax = '<th>Price (incl. tax)</th><td>£44.74</td>'
soup = BeautifulSoup(priceWithTax, 'html.parser')
print("The price of the book with tax is: " + soup.td.get_text())

priceNoTax = '<th>Price (excl. tax)</th><td>£44.74</td>'
soup = BeautifulSoup(priceNoTax, 'html.parser')
print("The price of the book without tax is: " + soup.td.get_text())

#Method 1 to get quantity available
"""
soup = BeautifulSoup(page.content, "html.parser")
quant = soup.find(string=re.compile("stock"))
print("The availability of the book is: " + quant)
"""
#Method 2 to get quantity available
quantity = '<td>In stock (14 available)</td>'
soup = BeautifulSoup(quantity, 'html.parser')
print("The availability of the book is: " + soup.td.get_text())

soup = BeautifulSoup(page.content, "html.parser")
content = soup.find(id='product_description').find_next_sibling()
#print(content)
description = content.get_text(strip=True)

print("The description of the book is: " + description)

# = content.css.select("div > ul > li > a:nth-of-type(2)")
#print(content)
content = soup.find('ul', class_="breadcrumb")
category = content.find_all("a")
print("The category of the book is: ", category[len(category)-1].get_text())
"""
for x in category:
    print(x)
    """

soup = BeautifulSoup(page.content, "html.parser")

content = soup.find('p', class_="star-rating Four")
print(content)
review = content.find()

content = soup.find("div", class_="item active")
#print(content)
image = content.find("img")
#print(image)
#print("The current review rating of the book is: " + image.get_text())

#Create header list
headers = ["product_page_url", "universal_ product_code (upc)", "book_title",
           "price_including_tax", "price_excluding_tax", "quantity_available",
           "product_description", "category", "review_rating", "image_url"]

#Create new CSV to write to
with open('Book.csv', 'w', newline = '') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(headers)
