import requests
import json
def getNews(company, loc):
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
      "apiKey": "db19b4bf-29e5-40cb-b319-4820814ea84c"
    }
    response = requests.get(url, request_body)
    data = response.json()
    with open('output.json','w') as f:
        json.dump(data,f,indent = 4)

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
