import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import yfinance as yf
import datetime as dt
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import date as Date
import numpy as np


### run Scraper(num_pages).scrape() to get trades

###creates a TradeList instance, which is a list of Trade objects

class Tickers():
    def getTickers(self):
        df = pd.read_excel('/Users/willpixley/Desktop/WebScraper/Stocks.xlsx')
        tickers = list(df.Ticker)
        industry = list(df.Industry)
        self.tickerD = {}
        for i in range(len(tickers)):
            self.tickerD[tickers[i]] = industry[i]
        return self.tickerD

HouseCommittees = {'Agriculture': {'Farm & Heavy Construction Machinery', 'Farm Products', 'Agricultural Inputs'}, 'Armed Services': {'Aerospace & Defense'}, 
'Banking and Financial Services': {'Banks-Regional', 'Insurance—Specialty', 'Asset Management', 'Banks—Diversified', 'Capital Markets', 'Insurance Brokers', 'Insurance—Diversified', 'Insurance—Reinsurance', 'Financial Data & Stock Exchanges', 'Financial Conglomerates', 'Credit Services', 'Insurance—Life, Insurance—Property & Casualty'}, 
'Education and Labor': {'Education & Training Services'}, 'Energy and Commerce': {'Oil & Gas Integrated', 'Oil & Gas Midstream', 'Thermal Coal', 'Oil & Gas Production', 'Oil & Gas E&P', 'Oil & Gas Drilling', 'Oil & Gas Equipment & Services', 'Oil & Gas Refining & Marketing', 'Uranium'}, 
'Financial Services': {'Banks-Regional', 'Insurance—Specialty', 'Insurance—Property & Casualty', 'Asset Management', 'Banks—Diversified', 'Capital Markets', 'Insurance Brokers', 'Insurance—Diversified', 'Insurance—Reinsurance', 'Financial Data & Stock Exchanges', 'Insurance—Life', 'Financial Conglomerates', 'Credit Services'}, 
'Foreign Affairs': {'Aerospace & Defense', 'Foreign Affairs'}, 'Homeland Security': {'Aerospace & Defense', 'Foreign Affairs'}, 
'Judiciary': {'Drug Manufacturers—Specialty & Generic', 'Drug Manufacturers—General'}, 
'Natural Resources': {'Oil & Gas Integrated', 'Oil & Gas Midstream', 'Thermal Coal', 'Oil & Gas Production', 'Other Industrial Metals & Mining', 'Oil & Gas E&P', 'Other Precious Metals & Mining', 'Oil & Gas Drilling', 'Oil & Gas Equipment & Services', 'Oil & Gas Refining & Marketing', 'Uranium'}, 
'Oversight and Reform': {'Footwear & Accessories', 'Information Technology Services', 'Leisure', 'Electronic Gaming & Multimedia', 'Luxury Goods', 'Discount Stores', 'Gambling', 'Restaurants', 'Travel Services', 'Auto Manufacturers', 'Packaging & Containers', 'Auto Parts', 'Textile Manufacturing', 'Tobacco', 'Internet Retail', 'Household & Personal Products', 'Internet Content & Information', 'Auto & Truck Dealerships', 'Pharmaceutical Retailers', 'Department Stores', 'Consulting Services', 'Specialty Retail', 'Recreational Vehicles', 'Entertainment', 'Advertising Agencies', 'Publishing', 'Home Improvement Retail', 'Broadcastings', 'Tools & Accessories'}, 
'Science, Space, and Technology': {'Semiconductor Equipment & Materials', 'Scientific & Technical Instruments', 'Solar', 'Communication Equipment', 'Biotechnology', 'Information Technology Services', 'Semiconductors', 'Electronic Components', 'Computer Hardware', 'Diagnostics & Research', 'Electrical Equipment & Parts'}, 
'Small Business': {'Specialty Business Services', 'Staffing & Employment Services'}, 
'Transportation and Infrastructure': {'Auto & Truck Dealerships', 'Marine Shipping', 'Airports & Air Services', 'Trucking', 'Railroads', 'Airlines', 'Waste Management', 'Infrastructure Operations', 'Engineering & Construction'}, 'Veterans Affairs': {'Aerospace & Defense'}
,'Intelligence': {'Aerospace & Defense', 'Foreign Affairs', 'Information Technology Services', 'Airports & Air Services'}}
SenateCommittees = {
    "Agriculture, Nutrition, and Forestry": {
        "Agricultural Inputs",
        "Farm Products"
    },
    'Education and the Workforce':{'Education & Training Services'},
    "Appropriations": {
        "Airports & Air Services",
        "Defense",
        "Education & Training Services",
        "Infrastructure Operations",
        "Packaged Foods",
        "Pollution & Treatment Controls",
        "Travel Services",
        "Utilities"},
    "Armed Services": {
        "Aerospace & Defense", "Defense"
    },
    'Budget': {'Banks-Regional', 'Insurance—Specialty', 
    'Asset Management', 'Banks—Diversified', 
    'Capital Markets', 'Insurance Brokers', 
    'Insurance—Diversified', 'Insurance—Reinsurance', 
    'Financial Data & Stock Exchanges', 'Financial Conglomerates', 
    'Credit Services', 'Insurance—Life', 'Insurance—Property & Casualty'}
    ,"Banking, Housing, and Urban Affairs": {
        "Asset Management",
        "Banks-Regional",
        "Banks—Diversified",
        "Credit Services",
        "Insurance Brokers",
        "Insurance—Diversified",
        "Insurance—Life",
        "Insurance—Property & Casualty",
        "Insurance—Reinsurance",
        "Mortgage Finance"
    },
    "Commerce, Science, and Transportation": {
        "Advertising Agencies",
        "Airlines",
        "Auto & Truck Dealerships",
        "Auto Manufacturers",
        "Auto Parts",
        "Broadcasting",
        "Business Equipment & Supplies",
        "Communication Equipment",
        "Computer Hardware",
        "Consumer Electronics",
        "Electronics & Computer Distribution",
        "Entertainment",
        "Internet Content & Information",
        "Internet Retail",
        "Lodging",
        "Medical Care Facilities",
        "Medical Devices",
        "Medical Distribution",
        "Medical Instruments & Supplies",
        "Publishing",
        "Railroads",
        "Scientific & Technical Instruments",
        "Security & Protection Services",
        "Semiconductor Equipment & Materials",
        "Semiconductors",
        "Telecom Services",
        "Textile Manufacturing",
        "Travel Services",
        "Trucking"
    },
    "Energy and Natural Resources": {
        "Coking Coal",
        "Oil & Gas Drilling",
        "Oil & Gas E&P",
        "Oil & Gas Equipment & Services",
        "Oil & Gas Integrated",
        "Oil & Gas Midstream",
        "Oil & Gas Production",
        "Oil & Gas Refining & Marketing",
        "Thermal Coal",
        "Uranium",
        "Utilities—Independent Power Producers",
        "Utilities—Regulated Electric",
        "Utilities—Regulated Gas",
        "Utilities—Regulated Water",
        "Utilities—Renewable"
    },
    "Environment and Public Works": {
        "Environmental Services","Oil & Gas Drilling",
        "Oil & Gas E&P",
        "Oil & Gas Equipment & Services",
        "Oil & Gas Integrated",
        "Oil & Gas Midstream",
        "Oil & Gas Production",
        "Oil & Gas Refining & Marketing",
        "Thermal Coal",
        "Pollution & Treatment Controls",
        "Waste Management"
    },
    "Finance": {
        "Financial Conglomerates","Thermal Coal",
        "Financial Data & Stock Exchanges"
    },
    "Foreign Relations": {
        "Integrated Freight & Logistics",
        "Marine Shipping", 'Foreign Affairs'
    },
    "Health, Education, Labor, and Pensions": {
        "Diagnostics & Research",
        "Education & Training Services",
        "Health Information Services",
        "Healthcare Plans",
        "Medical Care Facilities",
        "Medical Devices",
        "Medical Distribution",
        "Medical Instruments & Supplies",
        "Pharmaceutical Retailers","Drug Manufacturers—General",
        "Drug Manufacturers—Specialty & Generic",
    },
    "Homeland Security and Governmental Affairs": {
        "Security & Protection Services"
    },
    "Indian Affairs": {
        "Pollution & Treatment Controls"
    },
    "Judiciary": {
        "Broadcasting",
        "Consulting Services",
        "Drug Manufacturers—General",
        "Drug Manufacturers—Specialty & Generic",
        "Electronic Gaming & Multimedia",
        "Gambling",
        "Specialty Retail"
    },
    "Rules and Administration": {
        "Business Equipment & Supplies"
    },
    "Small Business and Entrepreneurship": {'N/A'}, "Veterans' Affairs": {"Aerospace & Defense", "Medical Care Facilities"}
    ,'Ways and Means':{'Utilities', 'Banks-Regional', 'Insurance—Specialty', 'Insurance—Property & Casualty', 'Asset Management', 'Banks—Diversified', 'Capital Markets', 'Insurance Brokers', 'Insurance—Diversified', 'Insurance—Reinsurance', 'Financial Data & Stock Exchanges', 'Insurance—Life', 'Financial Conglomerates', 'Credit Services'}}
   
fullCommittees = HouseCommittees | SenateCommittees
t = Tickers()
tickers = t.getTickers()



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
        self.date = datetime.strptime(date, '%Y-%m-%d').date()
        self.ticker = ticker 
        self.type = type 
        self.country = country
        self.link = link
        self.history = ''
        self.industry = self.getIndustry(tickers)
        self.pctChange = 0
        self.rating = 'N/A'
        

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
    


class Committees():
    def houseCommittees(self):
        df = pd.read_excel('/Users/willpixley/Desktop/WebScraper/House Committees.xlsx')
        committee_list = list(df.Committee)
        name_list = list(df.Last)
        for i in range(len(name_list)):
            name_list[i] = name_list[i].split(',')[0]
        self.fullDict = {name_list[i]:committee_list[i].split('|') for i in range(len(committee_list)) }
        
    def senateCommittees(self):
        df = pd.read_excel('/Users/willpixley/Desktop/WebScraper/SenateCommittees.xlsx')
        fullList = list(df.Committees)
        d = {}
        for i in range(len(fullList)):
            fullList[i] = fullList[i].strip()
            if fullList[i][-1] != ')':
                current = fullList[i]
                d[current] = []
            else:
                fullList[i] = fullList[i].split(',')
                d[current].append(fullList[i][0])
        for key in d:
            for i in range(len(d[key])):
                if d[key][i] in self.fullDict:
                    self.fullDict[d[key][i]].append(key)
                else:
                    self.fullDict[d[key][i]] = [key]
        
    def main(self):
        self.houseCommittees()
        self.senateCommittees()
        return self.fullDict


class TradeList():
    def __init__(self) -> None:
        self.tList = []
    
   
    def getattribute(self, __name: str) -> any:
        returnList = []
        for trade in self.tList:
            returnList.append(trade.getattribute(__name))
        return returnList
    def add(self, first, last, date, ticker, type, country, link):
        self.tList.append(Trade(first, last, date, ticker, type, country, link))
    
    def getBy(self, param: str, correct: str or int):
        returnList = []
        for trade in self.tList:
            try:
                if correct == trade.__getattribute__(param):
                    returnList.append(trade)
            except: 
                print("No such attribute")
        return returnList
    def __str__(self):
        s = ''
        for trade in self.tList:
            s += ' '+trade.__str__()
        return s
    
    def toExcel(self, filename):
        fullTrades = []
        for trade in self.tList:
            fullTrades.append(trade.getTradeInfo())
        df = pd.DataFrame(fullTrades, columns = ['Name', 'Type','Ticker','% Change', 'Rating', 'Industry', 'Date', 'Size', 'Link'] )
        df.to_excel(filename)
    
    def addTrade(self, trade):
        self.tList.append(trade)
    
   
    def getList(self):
        return self.tList








class Scraper():
    def __init__(self, pages, byWhat=False) -> None:
        self.pages = pages
        self.byPubDate='https://www.capitoltrades.com/trades?sortBy=-pubDate&page={}'
        self.byTradeDate = 'https://www.capitoltrades.com/trades?sortBy=-txDate&page={}'
        if byWhat:
            self.url = self.byPubDate
        else:
            self.url=self.byTradeDate
        self.tradeList = TradeList()
        self.tickers = Tickers().getTickers() ###dictionary of ticker:industry
        self.months = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,
        'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12 }
    def scrape(self):
        driver = webdriver.Chrome()        
        timerLength = .5
        for i in range(1, self.pages): #3366
            timerLength += .005
            url = self.url.format(i)
            driver.get(url)
            time.sleep(timerLength)
            tradeName = driver.find_elements(By.CLASS_NAME, 'q-fieldset.politician-name')
            tradeTicker = driver.find_elements(By.CLASS_NAME, 'q-field.issuer-ticker')
            tradeType = driver.find_elements(By.XPATH, "//*[contains(@class,'q-field tx-type tx-type--')]")
            tradeDate = driver.find_elements(By.CLASS_NAME, 'q-td.q-column--txDate')
            tradeSize = driver.find_elements(By.CLASS_NAME, "q-data-cell.trade-size")
            
            for i in range(len(tradeName)):
                xPath ='//*[@id="__next"]/div/div/div/article/section/div[2]/div[1]/table/tbody/tr[{}]/td[10]/a'.format(i+1)
                tradeLink = driver.find_element(By.XPATH, xPath)
                lastName = tradeName[i].text.split(' ')[-1].strip()
                firstName = tradeName[i].text.split(' ')[0].strip()
                link = tradeLink.get_attribute('href')
                date = tradeDate[i].text.replace('\n', ' ')
                date = date.split()
                date = dt.datetime(int(date[0]),self.months[date[2]], int(date[1]) )
                date = date.strftime("%Y-%m-%d")
                ticker = tradeTicker[i].text.split(":")[0]
                type = tradeType[i].text
                size = tradeSize[i].text
                try:
                    country = tradeTicker[i].text.split(":")[1]
                except:
                    country = 'N/A'
                t = Trade(firstName,lastName, date, ticker, type, country, link, size)
                self.tradeList.addTrade(t)


class Compare():
    def __init__(self, pages, byWhat=False) -> None:
        self.committee = Committees()
        self.Committees = self.committee.main()
        self.tickers = Tickers().getTickers() ###dictionary of ticker:industry
        self.scraper = Scraper(pages, byWhat=byWhat)
        self.scraper.scrape()
        self.storable = self.scraper.tradeList
        self.tradeList = self.scraper.tradeList.getList()
        self.sus = TradeList()
    
    def findOverlap(self):
        for trade in self.tradeList:
            ### list of committees the congressman is in
            try: 
                committees = self.Committees[trade.last]

            except: 
                print(trade.last)
                continue
            relevantIndustry = set()
            for c in committees:
                try:    
                    
                    relevantIndustry.update(fullCommittees[c])
                except: continue
            if trade.getIndustry(self.tickers) in relevantIndustry or trade.last == 'Pelosi': ### returns industry of the ticker
                self.sus.addTrade(trade) 
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

    
    
    
    

### each instance of scraper creates its own instance of TradeList
'''
s = Scraper(40)
s.scrape()
s.tradeList.toExcel('allTrades.xlsx')
'''


c = Compare(50, byWhat=True)
c.findGoodTrades()
c.storable.toExcel('TradesWithPrices4.xlsx')


### react native
