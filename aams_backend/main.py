import json
from fastapi import FastAPI
from NewsApi import getNews
from Sentiment import get_sentiment
from PriceData import getPriceData
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/stock/")
def everything(company:str,symbol:str):
    news_data,news_paras = getNews(company)
    news_sentiment = get_sentiment(news_paras)
    priceData = getPriceData(symbol)
    final_data = {
        "news_sentiment":news_sentiment,
        "news":news_data,
        "stock_data":priceData
    }
    return final_data
data = everything("RELIANCE INDUSTRIES","RELIANCE")
with open('output.json', 'w') as f:
    json.dump(data, f, indent=4)


