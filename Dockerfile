FROM python:3.11-slim

WORKDIR /web-scraper

COPY ./app /web-scraper/app
COPY ./requirements.txt /web-scraper/requirements.txt
COPY ./assessment2.py /web-scraper/assessment2.py

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/web-scraper/app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]