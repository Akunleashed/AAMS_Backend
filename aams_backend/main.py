from fastapi import FastAPI
from NewsApi import getNews
from Sentiment import get_sentiment
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
