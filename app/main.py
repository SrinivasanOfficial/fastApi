from fastapi import FastAPI, Query
import requests
from bs4 import BeautifulSoup

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Table Length Scraper API Running"}


@app.get("/tables")
def get_table_lengths(url: str = Query(..., description="Website URL")):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120 Safari/537.36"
    }

    response = requests.get(url, headers=headers, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")

    tables = soup.find_all("table")

    result = []
    for index, table in enumerate(tables):
        rows = table.find_all("tr")

        result.append({
            "table_index": index,
            "row_count": len(rows)
        })

    return {
        "url": url,
        "total_tables": len(tables),
        "tables": result
    }
