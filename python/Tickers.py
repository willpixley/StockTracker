import pandas as pd
import os

def getTickers() -> dict:
    filePath = os.path.join("Spreadsheets", "Stocks.xlsx")
    df = pd.read_excel(filePath)
    tickers = list(df.Ticker)
    industry = list(df.Industry)
    tickerD = {}
    for i in range(len(tickers)):
        tickerD[tickers[i]] = industry[i]
    return tickerD