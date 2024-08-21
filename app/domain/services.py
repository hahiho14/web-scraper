class ScrapingService:
    def __init__(self, scraper):
        self.scraper = scraper

    def scrape_articles(self, topic: str, pages: int):
        return self.scraper.scrape(topic, pages)
