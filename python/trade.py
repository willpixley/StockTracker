import datetime as dt
from datetime import datetime
import numpy as np
from dateutil.relativedelta import relativedelta
import python.Tickers as Tickers
import yfinance as yf

### pandas, selenium, webdriver, webdriver-manager, openpyxl, selenium.webdriver
class Trade(): ### first, last, date, ticker, type, country, link, size
    def __init__(self, first, last, date, ticker, type, country, link, volume) -> None:
        self.first = first
        self.last = last
        self.volume = volume.split('–')
        try:
            for i in range(len(self.volume)):
                if self.volume[i][-1] == 'K':
                    self.volume[i] = self.volume[i].replace('K', '')
                    self.volume[i] = int(self.volume[i]) * 1000
                else:
                    self.volume[i] = self.volume[i].replace('M', '')
                    self.volume[i] = int(self.volume[i]) * 1000000
        except:
            self.volume = 500
        self.volume = np.average(self.volume)   ### averages size range 
        # convert the date string to a date object
        self.date = datetime.strptime(date, '%m-%d-%Y').date()
        self.ticker = ticker 
        self.type = type 
        self.country = country
        self.link = link
        self.history = ''
        self.industry = self.getIndustry(Tickers.getTickers())
        self.pctChange = 0 
        self.rating = 'N/A'
        self.flag = False ### means there is industry/committee overlap
        

    def samePerson(self, t) -> bool:
        if self.last == t.last:
            return True
        return False
    def getPctChange(self):
            
            delta = relativedelta(datetime.now(), self.date)
            numMonths = delta.years * 12 + delta.months
            history = list(self.getStockHistory().Open)
            
            try: 
                self.pctChange = (history[-1]-history[0])/history[0] * 100
            except:
                self.pctChange = 0
            return self.pctChange, numMonths
    
    def getStockHistory(self):
        self.history = yf.download(self.ticker, self.date, dt.datetime.now())
        return self.history
    
    def getTradeInfo(self) -> list:
        return [self.first+' '+self.last,  self.type, self.ticker, self.pctChange, self.rating, self.industry, self.date,self.volume, self.link]

    def getIndustry(self, tickers: dict) -> str:
        try: industry = tickers[self.ticker]
        except: industry = 'Unknown'
        return industry
    
    def __str__(self):
        return '[{} {}, {}, {}, {}, {}, {}]'.format(self.first, self.last, self.type, self.ticker, self.date, self.country, self.link)    
    def getattribute(self, __name) -> any:
        return __name