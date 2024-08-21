from fastapi import FastAPI, Depends
from app.routes import router
from app.dependencies import get_scrape_use_case


app = FastAPI()

app.include_router(router, dependencies=[Depends(get_scrape_use_case)])
