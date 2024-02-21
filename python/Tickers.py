import os
import json
def getTickers() -> dict:
    ticker_file = os.path.join('json_files', 'tickers.json')
    with open(ticker_file, 'r') as f:
        tickerD = json.load(f)
    return tickerD

