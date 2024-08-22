import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from application.use_cases import ScrapeArticlesUseCase
from domain.services import ScrapingService
from infrastructure.repositories import ArticleRepository
from infrastructure.scraping import SeleniumScraper


scraper = SeleniumScraper()
scraping_service = ScrapingService(scraper)
repository = ArticleRepository()
scrape_use_case = ScrapeArticlesUseCase(scraping_service, repository)

def get_scrape_use_case():
    """Returns an instance of ScrapeArticlesUseCase.

    This function provides the initialized ScrapeArticlesUseCase 
    instance that is used to perform the web scraping task.

    Returns:
        ScrapeArticlesUseCase: The use case instance responsible for 
        executing the scraping operation.
    """
    return scrape_use_case
