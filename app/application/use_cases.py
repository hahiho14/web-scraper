from domain.services import ScrapingService

class ScrapeArticlesUseCase:
    """Handles the use case of scraping articles and saving them to a CSV file.

    Attributes:
        scraping_service (ScrapingService): The service responsible for scraping articles.
        repository: The repository for saving the scraped data.
    """
    def __init__(self, scraping_service: ScrapingService, repository):
        """Initializes ScrapeArticlesUseCase with the given services.

        Args:
            scraping_service (ScrapingService): The service responsible for scraping articles.
            repository: The repository for saving the scraped data.
        """
        self.scraping_service = scraping_service
        self.repository = repository

    def execute(self, topic: str, pages: int, file_path: str):
        """Executes the use case to scrape articles and save them to a CSV file.

        Args:
            topic (str): The topic to search for in the articles.
            pages (int): The number of pages to scrape.
            file_path (str): The path where the CSV file will be saved.

        Raises:
            Exception: If an error occurs during scraping or saving data.
        """
        data = self.scraping_service.scrape_articles(topic, pages)
        self.repository.save_to_csv(data, file_path)
