import json
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from news import getFinalData
from Sentiment import get_sentiment
from PriceData import getPriceData
from Final_analysis import getFinalAnalysis

app = FastAPI()
origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/stock/")
def everything(company:str,symbol:str):
    print(company)
    print(symbol)
    news_data,news_paras = getFinalData(company)
    news_sentiment = get_sentiment(news_paras)
    priceDataf,priceDatab = getPriceData(symbol)
    to_analyze={
        "data": priceDatab,
        "news":news_paras
    }
    analysis = getFinalAnalysis(json.dumps(to_analyze))
    final_data = {
        "news_sentiment":news_sentiment,
        "news":news_data,
        "stock_data":priceDataf,
        "analysis":analysis
    }
    return final_data

