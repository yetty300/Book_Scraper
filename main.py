import os

import requests
from bs4 import BeautifulSoup
import re
import csv

# Get main page URL that will be used to create html to work off of
page_url = "http://books.toscrape.com/"
info = requests.get(page_url)

# turn html into soup object that we will sort through
soup = BeautifulSoup(info.content, "html.parser")
#print(soup.prettify())
#books = soup.find_all('h3')
#print(books)
"""
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

"""
"""
category_url = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"
category_info = requests.get(category_url)
soup = BeautifulSoup(category_info.content, 'html.parser')

#This creates a for loop that gets info from each book on one page
books = soup.find_all('h3')
#print(books)
books_data = []
for book in books:
    book_url = book.find('a')['href'][9:] #problem is .../.../ so cut off leading 9 elements
    #print(book_url)
    book_info = requests.get('http://books.toscrape.com/catalogue/' + book_url) #instead of page_url + book_url
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
    books_data.append([book_url, upc, title, priceWithTax, priceNoTax, availability, description, category, rating,
                       image])

"""

#Creates list for data on all books on all pages
books_data = []
"""
for page_num in range(1, 51):
    url = f'http://books.toscrape.com/catalogue/page-{page_num}.html'
    #print(url)
    info = requests.get(url)
    #print(info)
    soup = BeautifulSoup(info.content, 'html.parser')
    print(soup)

    books = soup.find_all('h3')
    print(books)
"""

#categories = soup.find('ul', class_="nav nav-list").find('li').find('ul').find_all('a')
categories = soup.find('div', class_="side_categories").find_all('li')#soup.find('ul', class_="nav nav-list").find_all('li')
#print(categories)

for cat in categories[1:]:
    category_url = cat.find('a')['href']
    #print(category_url)
    category_info = requests.get(page_url + category_url)
    #print(category_info)
    category_soup = BeautifulSoup(category_info.content, 'html.parser')
    #print(category_soup)
    books = category_soup.find_all('h3')
    #print(books)
    # This creates a for loop that gets info from each book on page
    for book in books:
        book_url = book.find('a')['href'][9:]
        book_info = requests.get('http://books.toscrape.com/catalogue/' + book_url) #this needs fixing
        book_soup = BeautifulSoup(book_info.content, 'html.parser')

        upc = book_soup.find('table', class_="table table-striped").find_all('td')[0].text.strip()
        title = book_soup.find('h1').text
        priceWithTax = book_soup.find('table', class_="table table-striped").find_all('td')[2].text.strip()#.replace('£', '')
        priceNoTax = book_soup.find('table', class_="table table-striped").find_all('td')[3].text.strip()#.replace('£', '')
        category = book_soup.find('ul', class_="breadcrumb").find_all('a')[2].text.strip()
        rating = book_soup.find('p', class_="star-rating")['class'][1]
        availability = book_soup.find('p', class_="instock availability").text.strip()
        description = book_soup.find_all('p')[3].text.strip()
        #description = book_soup.find('div', id="product_description").find_next_sibling().text.strip()
        image = book_soup.find('div', class_="item active").find("img").get('src').strip()

        books_data.append([book_url, upc, title, priceWithTax, priceNoTax, availability, description, category, rating,
                           image])
        #print(books_data)
        # Create header list
        headers = ["product_page_url", "universal_ product_code (upc)", "book_title",
                   "price_including_tax", "price_excluding_tax", "quantity_available",
                   "product_description", "category", "review_rating", "image_url"]

        # Create new CSV to write to and add headers row
        with open(f'{category}.csv', 'w', encoding='utf-8', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(headers)

            for i in range(len(books_data)):
                row = books_data[i]
                writer.writerow(row)
    books_data.clear()






