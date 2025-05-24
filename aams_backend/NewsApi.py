import requests
def getNews(company):
    url = 'https://eventregistry.org/api/v1/article/getArticles'
    request_body = {
      "action": "getArticles",
      "keyword": company,
      "keywordLoc": "title",
      "categoryUri": ["dmoz/Business/Accounting","dmoz/Business/Business and Society","dmoz/Business/Associations","dmoz/Business/Business Services","dmoz/Business/Cooperatives","dmoz/Business/Financial Services","dmoz/Business/Marketing and Advertising","dmoz/Business/Business News and Media","dmoz/Business/Small Business","dmoz/Business/Wholesale Trade"],
      "categoryOper": "or",
      "sourceLocationUri": [
        "http://en.wikipedia.org/wiki/India"
      ],
      "ignoreSourceGroupUri": "paywall/paywalled_sources",
      "articlesPage": 1,
      "articlesCount": 10,
      "articlesSortBy": "date",
      "articlesArticleBodyLen": 10,
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
    return (response.json())