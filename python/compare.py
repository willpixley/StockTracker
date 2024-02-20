from python.TradeList import TradeList
from python.trade import Trade
from python.scraper import Scraper
import python.Tickers as Tickers
from python.committees import *

with open('Full_Committees.json', 'r') as json_file:
    fullCommittees = json.load(json_file)



senateAssignments = getSenateCommittee()
houseAssignments = getHouseCommittee()
congressmanByCommittee = senateAssignments | houseAssignments

class Compare():
    def __init__(self, pages, byWhat=False) -> None:
        self.tickers = Tickers.getTickers() ###dictionary of ticker:industry
        self.scraper = Scraper(pages, byWhat=byWhat) ## initializes scraper 
        self.scraper.scrape() ## begins webscraping process
        self.storable = self.scraper.tradeList ## initializes storable list for easy access
        self.tradeList = self.scraper.tradeList.getList() 
        self.sus = TradeList() # sus trades
    
    def findOverlap(self) -> None:
        for trade in self.tradeList:
            ### list of committees the congressman is in
            try: 
                committees = congressmanByCommittee[trade.last]
            except: 
                continue
            relevantIndustry = set()
            for c in committees:
                try:    
                    
                    relevantIndustry.update(fullCommittees[c])
                except: continue
            if trade.getIndustry(self.tickers) in relevantIndustry: ### returns industry of the ticker
                trade.flag = True 
        
    def classifyTrade(self, trade: Trade) -> None:
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
    
    
    def findGoodTrades(self) -> None:
        for trade in self.tradeList:
            self.classifyTrade(trade)


    
    def toExcel(self, filename: str) -> None:
        self.sus.toExcel(filename)