from fastapi import FastAPI, Query
import requests
from bs4 import BeautifulSoup
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Web Scraper API is running"}


@app.get("/scrape")
def scrape_url(url: str = Query(..., description="Website URL to scrape")):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    return HTMLResponse(content=f"<pre>{response.text}</pre>")
