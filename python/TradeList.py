'''
TradeList stores scraped trades


'''


from python.trade import Trade
import pandas as pd
from styleframe import StyleFrame, Styler, utils
class TradeList():
    def __init__(self) -> None:
        self.tList = []
    
   
    def getattribute(self, __name: str) -> any:
        returnList = []
        for trade in self.tList:
            returnList.append(trade.getattribute(__name))
        return returnList
    
    def add(self, first, last, date, ticker, type, country, link) -> None:
        self.tList.append(Trade(first, last, date, ticker, type, country, link))
    
    def getBy(self, param: str, correct: str or int) -> list:
        returnList = []
        for trade in self.tList:
            try:
                if correct == trade.__getattribute__(param):
                    returnList.append(trade)
            except: 
                print("No such attribute")
        return returnList
    def __str__(self) -> str:
        s = ''
        for trade in self.tList:
            s += ' '+trade.__str__()
        return s
    
    def extendTrades(self, newList) -> None:
        for trade in newList:
            self.addTrade(trade)
    
    def toExcel(self, filename) -> None:
        fullTrades = []
        indicies = []

        for i in range(len(self.tList)):
            if self.tList[i].flag:
                indicies.append(i)
            fullTrades.append(self.tList[i].getTradeInfo())
        df = pd.DataFrame(fullTrades, columns = ['Name', 'Type','Ticker','% Change', 'Rating', 'Industry', 'Date', 'Size', 'Link'] )
        sf = StyleFrame(df)
        print(indicies)
        sketchy_style = Styler(bg_color=utils.colors.red, font_color=utils.colors.white)
        sf.apply_style_by_indexes(indicies, styler_obj=sketchy_style)
        sf.to_excel(filename).save()


    
    def addTrade(self, trade) -> None:
        self.tList.append(trade)
    
   
    def getList(self) -> list:
        return self.tList