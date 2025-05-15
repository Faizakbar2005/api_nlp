from fastapi import APIRouter, Query
from app.services.rss_parser import fetch_news

router = APIRouter()

@router.get("/search")
def search_news(q: str = Query(..., min_length=1)):
    return fetch_news(q)
