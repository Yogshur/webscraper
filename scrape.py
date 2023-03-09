import requests
from bs4 import BeautifulSoup
import schedule
import time
import re


def scrape_website():
    url = 'https://www.topstocktips.com/tipbn'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Get the page title
    title = soup.title.text
    print(f"Page title: {title}")
    
    # Get the compensation message
    compensation_element = soup.find('span', text=re.compile('We have been compensated up to'))
    if compensation_element is not None:
        compensation_text = compensation_element.text
        print(f"Compensation message: {compensation_text}")
        
schedule.every().minute.do(scrape_website)

while True:
    schedule.run_pending()
    time.sleep(1)