import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver_path = os.path.join(os.getcwd(), 'driver', 'chromedriver')

if not os.path.isfile(driver_path):
    raise FileNotFoundError(f"WebDriver executable not found at {driver_path}")

class SeleniumScraper:
    """A web scraper that uses Selenium to extract article data from a website.

    Attributes:
        driver (webdriver.Chrome): The Selenium WebDriver instance for Chrome.
        wait (WebDriverWait): An instance of WebDriverWait to handle explicit waits.
    """
    def __init__(self):
        """Initializes the SeleniumScraper with headless Chrome options and sets up the WebDriver."""
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")

        chrome_service = Service(executable_path=driver_path)
        self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)

    def scrape(self, topic: str, pages: int):
        """Scrapes articles from a detik.com based on the provided topic and number of pages.

        Args:
            topic (str): The search query topic to scrape articles for.
            pages (int): The number of pages to scrape.

        Returns:
            list: A list of dictionaries containing the scraped article data. Each dictionary
            contains the article's ID, title, subtitle, content, and date.

        Raises:
            Exception: If an error occurs during scraping, the WebDriver is quit, and the exception is raised.
        """
        data = []
        article_id = 1
        for page in range(1, pages + 1):
            self.driver.get(f'https://www.detik.com/search/searchall?query={topic}&page={page}&result_type=relevansi')

            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.media__desc')))
            
            articles = self.driver.find_elements(By.CSS_SELECTOR, 'article')
            time.sleep(2)

            last_height = self.driver.execute_script('return document.body.scrollHeight')

            while True:
                self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
                time.sleep(2)
                new_height = self.driver.execute_script('return document.body.scrollHeight')
                if new_height == last_height:
                    break
                last_height = new_height

            soup = BeautifulSoup(self.driver.page_source, 'lxml')
            articles = soup.find_all('article', class_='list-content__item')

            for article in articles:
                title_tag = article.select_one('h3 > a')
                title = title_tag.get_text(strip=True) if title_tag else 'N/A'
                subtitle_tag = article.find('h2')
                subtitle = subtitle_tag.get_text(strip=True) if subtitle_tag else 'N/A'
                content_tag = article.select_one('div.media__desc')
                content = content_tag.get_text(strip=True) if content_tag else 'N/A'
                date_tag = article.select_one('div.media__date span')
                date = date_tag.get('title', 'N/A') if date_tag else 'N/A'

                data.append({
                    'id': article_id,
                    'Title': title,
                    'Subtitle': subtitle,
                    'Content': content,
                    'Date': date
                })
                
                article_id += 1

        self.driver.quit()
        return data
