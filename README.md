# Web Scraper

## Project Description

The Web Scraper project is designed to extract articles from a website and save the data into a CSV file. It leverages Selenium for web scraping and FastAPI to expose an endpoint that initiates the scraping process. The project is structured using Domain-Driven Design (DDD) principles, focusing on clear separation between different components such as the scraper, service, repository, and use case.

### Features

- **Web Scraping**: Utilizes Selenium to scrape article information.
- **API Endpoint**: FastAPI provides an endpoint to trigger the scraping.
- **CSV Export**: Saves scraped data into a CSV file.

## Project Structure

- `app/`: Contains FastAPI application code.
  - `main.py`: The entry point of the FastAPI application. Configures the API and dependencies.
  - `routes.py`: Defines API routes and request handling.
- `domain/`: Core business logic and domain models.
  - `services.py`: Contains the `ScrapingService` class that coordinates scraping.
  - `models.py`: Defines the `Article` class.
- `dependencies.py`: Provides dependency injection for the FastAPI application.
- `driver/`: Directory for WebDriver executables (e.g., `chromedriver`).
- `requirements.txt`: Lists Python dependencies required for the project.
- `Dockerfile`: Docker configuration for containerizing the application.

## Prerequisites

- Python 3.10 or higher
- Docker (optional, for containerized execution)
- WebDriver (e.g., ChromeDriver) for Selenium

## Setup and Running Locally

### 1. Clone the Repository

```bash
git clone https://github.com/hahiho14/web-scraper.git
cd web-scraper
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Download WebDriver
Download the WebDriver for your browser (e.g., ChromeDriver) and place it in the `driver` directory of the project.

### 5. Run the FastAPI Server
```
uvicorn app.main:app --reload
```
The FastAPI server will start and listen at http://localhost:8000.

### 6. Test the API
To test the API, use curl or Postman. Example using curl:
```
curl "http://localhost:8000/scrape?topic=technology&pages=1"
```

## Running with Docker
### 1. Build the Docker Image
Ensure Docker is installed and build the Docker image with:
```
docker build -t web-scraper .
```

### 2. Run the Docker Container
Run the Docker container using:
```
docker run -p 8000:8000 --name web-scraper-container web-scraper
```

## Running with Docker Compose
### 1. Ensure Docker Compose is Installed
Make sure Docker Compose is installed on your machine. You can download it from Docker's website.

### 2. Run docker-compose.yaml File
You need to run `docker-compose.yaml` by simply doing this:
```
docker-compose build
docker-compose up -d
```

The application will be accessible at http://localhost:8000.

## API Endpoint
### `GET /scrape`
- **Description**: Initiates the scraping process based on the provided topic and number of pages.
- **Parameters**:
    - topic (str): The topic to search for.
    - pages (int): The number of pages to scrape.
- **Response**:
    - 200 OK: If the scraping is successful.
    - 500 Internal Server Error: If an error occurs during scraping.

For detail documentation you can use swagger by simply go to http://localhost:8000/docs .

## Contributing
Contributions are welcome! Please submit issues or pull requests if you find any bugs or have improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

```python
This `README.md` includes detailed information about the project, its structure, setup instructions for both Python and Docker, and API usage. Feel free to adjust any specific details or add further information as needed.
```
