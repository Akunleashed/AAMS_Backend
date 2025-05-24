import requests
def getPriceData(company:str):
    url = "https://indian-stock-exchange-api2.p.rapidapi.com/stock"
    querystring = {"name":company}
    headers = {
        "x-rapidapi-key": "3c82134103msh75f889c1e52fa98p114a12jsn040c8e3cc602",
        "x-rapidapi-host": "indian-stock-exchange-api2.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    name = data["companyName"]
    fundamentals = data["companyProfile"]["peerCompanyList"][0]
    for i in data["companyProfile"]["peerCompanyList"]:
        if(i["companyName"]==name):
            fundamentals = i
            break
    dataToFrontend = {
        "CompanyName": data["companyName"],
        "Description":data["companyProfile"]["companyDescription"],
        "CurrentPriceBSE":data["currentPrice"]["BSE"],
        "CurrentPriceNSE":data["currentPrice"]["NSE"],
        "52weekHigh":data["yearHigh"],
        "52weekLow":data["yearLow"],
        "priceToBookValueRatio": fundamentals["priceToBookValueRatio"],
        "priceToEarningsValueRatio":fundamentals["priceToEarningsValueRatio"],
        "marketCap":fundamentals["marketCap"],
        "returnOnAverageEquity5YearAverage":fundamentals["returnOnAverageEquity5YearAverage"],
        "returnOnAverageEquityTrailing12Month":fundamentals["returnOnAverageEquityTrailing12Month"],
        "ltDebtPerEquityMostRecentFiscalYear":fundamentals["ltDebtPerEquityMostRecentFiscalYear"],
        "netProfitMargin5YearAverage":fundamentals["netProfitMargin5YearAverage"],
        "netProfitMarginPercentTrailing12Month":fundamentals["netProfitMarginPercentTrailing12Month"],
        "dividendYieldIndicatedAnnualDividend":fundamentals["dividendYieldIndicatedAnnualDividend"],
    }
    return dataToFrontend