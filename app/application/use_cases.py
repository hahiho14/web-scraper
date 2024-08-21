from domain.services import ScrapingService

class ScrapeArticlesUseCase:
    def __init__(self, scraping_service: ScrapingService, repository):
        self.scraping_service = scraping_service
        self.repository = repository

    def execute(self, topic: str, pages: int, file_path: str):
        data = self.scraping_service.scrape_articles(topic, pages)
        self.repository.save_to_csv(data, file_path)
