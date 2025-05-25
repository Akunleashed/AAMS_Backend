import requests
import json
def getPriceData(company:str):
    url = "https://indian-stock-exchange-api2.p.rapidapi.com/stock"
    querystring = {"name":company}
    headers = {
        "x-rapidapi-key": "f2e7efde81msh8b0c0390cfcfbb2p19b315jsnea580d852aa4",
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
        "dividendYieldIndicatedAnnualDividend":fundamentals["dividendYieldIndicatedAnnualDividend"]
        
    }
    dataToBackend = {
        "CompanyName": data["companyName"],
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
        "financials":data["financials"],
        "shareholding":data["shareholding"],
        "historicalData":data["stockTechnicalData"],
        "keyMetrics":data["keyMetrics"],
        "analystView":data["analystView"],
        "peerCompanyList":data["companyProfile"]["peerCompanyList"]

    }

    return dataToFrontend,dataToBackend
getPriceData("Reliance")