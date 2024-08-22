from fastapi import APIRouter, Depends
from application.use_cases import ScrapeArticlesUseCase
from fastapi.responses import JSONResponse

from app.dependencies import get_scrape_use_case


router = APIRouter()

@router.get("/scrape")
async def scrape_articles(topic: str, pages: int, scrape_use_case: ScrapeArticlesUseCase = Depends(get_scrape_use_case)):
    """Initiates the web scraping process for a given topic and number of pages.

    Args:
        topic (str): The topic to search and scrape articles for.
        pages (int): The number of pages to scrape.
        scrape_use_case (ScrapeArticlesUseCase): The use case instance responsible for executing the scraping logic.

    Returns:
        JSONResponse: A JSON response indicating the success or failure of the scraping process.

    Raises:
        Exception: If an error occurs during the scraping process, it is caught and returned in the response.
    """
    file_path = f"data/scraped_data.csv"
    try:
        scrape_use_case.execute(topic, pages, file_path)
        return JSONResponse(content={"message": "Scraping initiated successfully"}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)