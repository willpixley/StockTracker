from python.TradeList import TradeList
from python.scraper import Scraper
import python.Tickers as Tickers
from python.committees import *

class Compare():
    def __init__(self, pages, byWhat=False) -> None:
        self.tickers = Tickers.getTickers() ###dictionary of ticker:industry
        self.scraper = Scraper(pages, byWhat=byWhat)
        self.scraper.scrape()
        self.storable = self.scraper.tradeList
        self.tradeList = self.scraper.tradeList.getList()
        self.sus = TradeList()
    
    def findOverlap(self):
        for trade in self.tradeList:
            ### list of committees the congressman is in
            try: 
                committees = fullCommittees[trade.last]

            except: 
                print(trade.last)
                continue
            relevantIndustry = set()
            for c in committees:
                try:    
                    
                    relevantIndustry.update(fullCommittees[c])
                except: continue
            if trade.getIndustry(self.tickers) in relevantIndustry: ### returns industry of the ticker
                trade.flag = True 
    def findGoodTrades(self):
        for trade in self.tradeList:
            pctChange, numMonths = trade.getPctChange()
            lowReturn = (1.01**numMonths-1)*100
            highReturn=(1.025**numMonths-1)*100
            if trade.type == 'SELL':
                if pctChange > 0:
                    trade.rating = 'Bad'
                elif pctChange == 0:
                    trade.rating = 'N/A'
                elif pctChange > -lowReturn:
                    trade.rating = 'Ok'
                elif pctChange >= -highReturn:
                    trade.rating = 'Good'
                elif pctChange < -highReturn:
                    trade.rating = 'Very Good'
            else:
                if pctChange < 0:
                    trade.rating = 'Bad'
                elif pctChange == 0:
                    trade.rating = 'N/A'
                elif pctChange < lowReturn:
                    trade.rating = 'Ok'
                elif pctChange <= highReturn:
                    trade.rating = 'Good'
                elif pctChange > highReturn:
                    trade.rating = 'Very Good'

    
    def toExcel(self, filename):
        self.sus.toExcel(filename)