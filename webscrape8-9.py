import requests
from bs4 import BeautifulSoup
import schedule
import time
from datetime import datetime
import pytz

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

def job():
    eastern = pytz.timezone('US/Eastern')
    current_time = datetime.now(eastern)
    if current_time.hour == 8:
        for minute in range(current_time.minute, 60):
            schedule.every().day.at(f"08:{minute:02d}").do(scrape_website)
    elif current_time.hour == 9:
        for minute in range(0, current_time.minute+1):
            schedule.every().day.at(f"09:{minute:02d}").do(scrape_website)

while True:
    job()
    schedule.run_pending()
    time.sleep(1)