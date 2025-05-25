import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def getNews(company,loc):
    url = 'https://eventregistry.org/api/v1/article/getArticles'
    request_body = {
      "action": "getArticles",
      "keyword": company,
      "keywordLoc": loc,
      "categoryUri": ["dmoz/Business/Accounting","dmoz/Business/Business and Society","dmoz/Business/Associations","dmoz/Business/Business Services","dmoz/Business/Cooperatives","dmoz/Business/Financial Services","dmoz/Business/Marketing and Advertising","dmoz/Business/Business News and Media","dmoz/Business/Small Business","dmoz/Business/Wholesale Trade"],
      "categoryOper": "or",
      "sourceLocationUri": [
        "http://en.wikipedia.org/wiki/India"
      ],
      "ignoreSourceGroupUri": "paywall/paywalled_sources",
      "articlesPage": 1,
      "articlesCount": 10,
      "articlesSortBy": "date",
      "articlesArticleBodyLen": 2000,
      "isDuplicateFiler": "skipDuplicates",
      "lang": "eng",
      "dataType": [
        "news",
        "pr"
      ],
      "forceMaxDataTimeWindow": 7,
      "resultType": "articles",
      "apiKey": API_KEY
    }
    response = requests.get(url, request_body)
    data = response.json()
    paragraphs = []

    looped = data["articles"]["results"]

    for content in looped:
      paragraphs.append(content["body"])


    dictionary = {}

    for i,content in enumerate(looped):
       short = content["body"][:200]
       dictionary[i] = {
          "title" : content["title"],
          "link" : content["url"],
          "body" : short + "..."
       }

    return dictionary, paragraphs

def getFinalData(company):
    a,b = getNews(company,"title")
    if(len(a)<5):
        a,b=getNews(company,"body")
    return a,b
