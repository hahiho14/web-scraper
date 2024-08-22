class ScrapingService:
    """A service class for scraping articles using a scraper instance.

    Attributes:
        scraper (SeleniumScraper): An instance of SeleniumScraper used for web scraping.
    """
    def __init__(self, scraper):
        """Initializes the ScrapingService with a given scraper.

        Args:
            scraper (SeleniumScraper): An instance of SeleniumScraper for scraping articles.
        """
        self.scraper = scraper

    def scrape_articles(self, topic: str, pages: int):
        """Scrapes articles based on the provided topic and number of pages.

        Args:
            topic (str): The topic to search for in articles.
            pages (int): The number of pages to scrape.

        Returns:
            list: A list of dictionaries containing article data.
        """
        return self.scraper.scrape(topic, pages)
