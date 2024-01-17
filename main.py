import requests
from bs4 import BeautifulSoup
import csv

# Get main page URL that will be used to create html to work off of
page_url = "http://books.toscrape.com/"
info = requests.get(page_url)

# turn html into soup object that we will sort through
soup = BeautifulSoup(info.content, "html.parser")
#print(soup.prettify())
books = soup.find_all('h3')
#print(books)

#this gets information from one book
book_url = "http://books.toscrape.com/catalogue/sorting-the-beef-from-the-bull-the-science-of-food-fraud-forensics_736/index.html"
book_info = requests.get(book_url)
book_soup = BeautifulSoup(book_info.content, 'html.parser')

upc = book_soup.find('table', class_="table table-striped").find_all('td')[0].text.strip()
#print(upc)
title = book_soup.find('h1').text
#print(title)
priceWithTax = book_soup.find('table', class_="table table-striped").find_all('td')[2].text.strip()
#print(priceWithTax)
priceNoTax = book_soup.find('table', class_="table table-striped").find_all('td')[3].text.strip()
#print(priceNoTax)
category = book_soup.find('ul', class_="breadcrumb").find_all('a')[2].text.strip()
#print(category)
rating = book_soup.find('p', class_="star-rating")['class'][1]
#print(rating)
availability = book_soup.find('p', class_="instock availability").text.strip()
#print(availability)
description = book_soup.find('div', id="product_description").find_next_sibling().text.strip()
#print(description)
image = book_soup.find('div', class_="item active").find("img").get('src').strip()
#print(image)
#print(' ')

#This creates a for loop that gets info from each book on one page
for book in books:
    book_url = book.find('a')['href']
    #print(book_url)
    book_info = requests.get(page_url + book_url) #maybe add +page_url
    #print(book_info)
    book_soup = BeautifulSoup(book_info.content, 'html.parser')

    upc = book_soup.find('table', class_="table table-striped").find_all('td')[0].text.strip()
    #print(upc)
    title = book_soup.find('h1').text
    #print(title)
    priceWithTax = book_soup.find('table', class_="table table-striped").find_all('td')[2].text.strip()
    #print(priceWithTax)
    priceNoTax = book_soup.find('table', class_="table table-striped").find_all('td')[3].text.strip()
    #print(priceNoTax)
    category = book_soup.find('ul', class_="breadcrumb").find_all('a')[2].text.strip()
    #print(category)
    rating = book_soup.find('p', class_="star-rating")['class'][1]
    #print(rating)
    availability = book_soup.find('p', class_="instock availability").text.strip()
    #print(availability)
    description = book_soup.find('div', id="product_description").find_next_sibling().text.strip()
    #print(description)
    image = book_soup.find('div', class_="item active").find("img").get('src').strip()
    #print(image)
    #print(' ')

#Creates list for data on all books on all pages
books_data = []
for page_num in range(1, 51):
    url = f'http://books.toscrape.com/catalogue/page-{page_num}.html'
    print(url)
    info = requests.get(url)
    soup = BeautifulSoup(info.content, 'html.parser')

    books = soup.find_all('h3')
    print(books)

    # This creates a for loop that gets info from each book on page
    for book in books:
        book_url = book.find('a')['href']
        book_info = requests.get(page_url + book_url)
        book_soup = BeautifulSoup(book_info.content, 'html.parser')

        upc = book_soup.find('table', class_="table table-striped").find_all('td')[0].text.strip()
        title = book_soup.find('h1').text
        priceWithTax = book_soup.find('table', class_="table table-striped").find_all('td')[2].text.strip()
        priceNoTax = book_soup.find('table', class_="table table-striped").find_all('td')[3].text.strip()
        category = book_soup.find('ul', class_="breadcrumb").find_all('a')[2].text.strip()
        rating = book_soup.find('p', class_="star-rating")['class'][1]
        availability = book_soup.find('p', class_="instock availability").text.strip()
        description = book_soup.find('div', id="product_description").find_next_sibling().text.strip()
        image = book_soup.find('div', class_="item active").find("img").get('src').strip()

        books_data.append([upc, title, category, priceWithTax, priceNoTax, availability, description, category, rating,
                           image])
        print(books_data)


"""
content = soup.find('article', class_='product_pod')

#Retrieve the url of book
book_url = "http://books.toscrape.com/catalogue/sorting-the-beef-from-the-bull-the-science-of-food-fraud-forensics_736/index.html"
print(book_url)

#Method 1 of getting UPC
book_upc= soup.find('td').get_text()
print("The upc code of the book is: " + book_upc)
#Method 2 of getting UPC
upc = soup.table.td
print("The upc code of the book is: " + upc.string)

#Get the title of the book
book_titles = soup.title
print("The title of the book is: " + book_titles.get_text(strip=True))

#Get the price with Tax
priceWithTax = '<th>Price (incl. tax)</th><td>£44.74</td>'
soup = BeautifulSoup(priceWithTax, 'html.parser')
print("The price of the book with tax is: " + soup.td.get_text())

#Get the price without Tax
priceNoTax = '<th>Price (excl. tax)</th><td>£44.74</td>'
soup = BeautifulSoup(priceNoTax, 'html.parser')
print("The price of the book without tax is: " + soup.td.get_text())

#Method 1 to get quantity available

soup = BeautifulSoup(page.content, "html.parser")
quant = soup.find(string=re.compile("stock"))
print("The availability of the book is: " + quant)


#Method 2 to get quantity available
quantity = '<td>In stock (14 available)</td>'
soup = BeautifulSoup(quantity, 'html.parser')
print("The availability of the book is: " + soup.td.get_text())

#Get the description of the Book
soup = BeautifulSoup(page.content, "html.parser")
content = soup.find(id='product_description').find_next_sibling()
description = content.get_text(strip=True)
print("The description of the book is: " + description)

#Geth the category of the Book
content = soup.find('ul', class_="breadcrumb")
category = content.find_all("a")
print("The category of the book is: ", category[len(category)-1].get_text())

#redefine the soup to allow for searching
soup = BeautifulSoup(page.content, "html.parser")

#To get the review of the Book
content = soup.find('p', class_="star-rating Four")
print("The rating of the book is: " + content.name)
#review = content
#print(review)

#To get the review URL
content = soup.find("div", class_="item active")
image = content.find("img")
print("The image url is: " +image.get('src'))

#lists to hold needed categorys
TITLES = []
for title in book_titles:
    TITLES.append(title)
URLS = []
for url in book_url:
    URLS.append(url)
    print(URLS)
UPCS = []
for upc in book_upc:
    UPCS.append(upc)
PRICES_WTAX = []
for price in priceWithTax:
    PRICES_WTAX.append(price)
PRICES_NTAX = []
for price in priceNoTax:
    PRICES_NTAX.append(price)
QUANTITY = []
for num in quantity:
    QUANTITY.append(num)
DESCRIPTIONS = []
for info in description:
    DESCRIPTIONS.append(description)
CATEGORIES = []
for cat in category:
    CATEGORIES.append(cat)
RATINGS = []
for title in book_titles:
    RATINGS.append(title)
IMAGE_URLS =[]
for link in image:
    IMAGE_URLS.append(link)

#Create header list
headers = ["product_page_url", "universal_ product_code (upc)", "book_title",
           "price_including_tax", "price_excluding_tax", "quantity_available",
           "product_description", "category", "review_rating", "image_url"]

#Create new CSV to write to and add headers row
with open('Book.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(headers)

    for i in range(len(TITLES)):
        print(TITLES)
        row = [URLS[i], UPCS[i], TITLES[i], PRICES_WTAX[i], PRICES_NTAX[i], QUANTITY[i], DESCRIPTIONS[i], CATEGORIES[i], RATINGS[i], IMAGE_URLS[i]]
        writer.writerow(row)

"""