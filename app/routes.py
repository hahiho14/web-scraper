from fastapi import APIRouter, Depends
from application.use_cases import ScrapeArticlesUseCase
from fastapi.responses import JSONResponse

from app.dependencies import get_scrape_use_case


router = APIRouter()

@router.get("/scrape")
async def scrape_articles(topic: str, pages: int, scrape_use_case: ScrapeArticlesUseCase = Depends(get_scrape_use_case)):
    file_path = f"data/scraped_data.csv"
    try:
        scrape_use_case.execute(topic, pages, file_path)
        return JSONResponse(content={"message": "Scraping initiated successfully"}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)