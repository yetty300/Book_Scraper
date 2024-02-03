# Python Book Scraper Program
This is a beginner/intermediate friendly program that pulls data from the website http:books.toscrape.com and uploads it as an excel doc for readability. 
This project will help you learn how to read HTML and use a couple of different Python Packages (BeautifulSoup, OS, requests, csv ...). 
The project does require a basic understanding of the python programming language such as how to make lists and use loops. I highly recommend reviewing the documentation and trying a couple of exercises on replit if needed.

## The Program
This program pulls data from the website http://books.toscrape.com and organizes it into various categories to be exported to CSV/excel files for easy viewing and organizing. 
The pieces of data it retrieves for each book are: title, URL, UPC, price w/tax and without, description, category, rating and image URL and images. 
It organizes these pieces of data into multiple excel files by category. The reason for this program is it makes viewing relevant pieces of data from a entire website straightforward and quick. 
Instead of scrolling through page after page of books all that data is assembled for you to easily search through. 
It eliminates the time component and retrieves a vast amount of data which can help you quickly find the necessary data that you need regarding whatever book you are trying to find. 
This project can be adapted for future projects to scrape a number of different websites (please make sure that you can do so legally)

### Setting up the IDE (if preferred):
1. Go to https://www.jetbrains.com/pycharm/ version 3.12 and download the program for your given operating system. 
2. Download python from https://www.python.org/downloads/ version 3.12.1 for your specific operating system. 
3. Open it and create a new project
4. Download the code
5. Extract the code to preferred location
6. In the IDE go to file open and navigate to the location you extracted the code from and select the main.py
    (optional) Navigate the the extracted folder location and double click the main.py file and it will run automtically in the terminal

### Instructions for Terminal (Windows):
1. Download files from this repository or create a clone using the code below.

    $ git clone https://github.com/yetty300/Book_Scraper

2. Navigate to the directory containing the repository.

    $ cd Book_Scraper

3. Using these terminal commands, create and activate a virtual environment.

    $ python -m venv env

    $ env/scripts/activate (this step may be required for some)

5. Use the command below to install the packages according to the configuration file requirements.txt.

    $ pip install -r requirements.txt

6. Open and run the file allcategories.py to download product data in CSV format and product images.

    $ .\main.py

### Instructions for Mac:

1. Download files from this repository or create a clone using the code below.

   $ git clone https://github.com/yetty300/Book_Scraper

2. Navigate to the directory containing the repository.

    $ cd Book_Scraper

3. Using these terminal commands, create and activate a virtual environment.

    $ python -m venv env

    $ source env/bin/activate

4. Use the command below to install the packages according to the configuration file requirements.txt.

    $ python3 -m pip install -r requirements.txt

5. Open and run the file allcategories.py to download product data in CSV format and product images.

    $ python main.py
