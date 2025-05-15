from fastapi import FastAPI
from app.routes import news

app = FastAPI()

app.include_router(news.router)

@app.get("/")
def root():
    return {"message": "API pencarian berita dengan RSS Google News"}
