"""
A web scraper scrapes/gets data from
webpages and saves it in any format we want, either .csv or .txt.
Web scraping is a term for using a program to download and
process content from the web. Make sure to install requests and beautifulsoup4 using "pip install requests" and "pip install beautifulsoup4"
"""
import requests
from bs4 import BeautifulSoup

# set url from webpage you want to scrape
url = 'https://www.example.com'

# send an HTTP request to url and retrieve content
response = requests.get(url)

# create BeautifulSoup object that parses HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# find all links on the webpage
links = soup.find_all('a')

# print text and href attributes of each link
for link in links:
    print(link.get('href'), link.text)

