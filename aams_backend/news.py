import requests
import json

API_KEY = "pub_7d72e6bf846d4db5bd3ae5af7ddcfd35"

def getNews(company,Q):
    url = f"https://newsdata.io/api/1/latest?apikey={API_KEY}&{Q}={company}&country=in&language=en"
    response = requests.get(url)
    data = response.json()
    paragraphs = []
    looped = data["results"]
    for c in looped:
        paragraphs.append(c["description"])
    
    dictionary = {}
    for i,c in enumerate(looped):
        short = c["description"]
        dictionary[i] = {
            "title": c["title"],
            "link": c["link"],
            "body":  short + "..."
        }
    
    return dictionary, paragraphs

def getFinalData(company):
    a,b = getNews(company, "qInTitle")
    if(len(a) < 5):
        a,b=getNews(company,"qInMeta")
    return a,b


