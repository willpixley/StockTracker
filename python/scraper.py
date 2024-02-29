from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime as dt
import python.Tickers as Tickers
from python.TradeList import TradeList
from python.trade import Trade
from selenium.webdriver.chrome.options import Options

class Page():
    def __init__(self, url, driver) -> None:
        self.url = url
        self.driver = driver
        self.tradeNames = []
        self.tradeTickers = []
        self.tradeTypes = []
        self.tradeTypes = []
        self.tradeDates = []
        self.tradeSizes = []
        self.tradeLinks = []
        self.months = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,
        'Aug':8,'Sept':9,'Oct':10,'Nov':11,'Dec':12 }


    def _getListsPerPage(self, url) -> int:
        self.driver.get(url)
        time.sleep(1)
        self.tradeNames = self.driver.find_elements(By.CLASS_NAME, 'q-fieldset.politician-name')
        self.tradeTickers = self.driver.find_elements(By.CLASS_NAME, 'q-field.issuer-ticker')
        self.tradeTypes = self.driver.find_elements(By.XPATH, "//*[contains(@class,'q-field tx-type tx-type--')]")
        self.tradeDates = self.driver.find_elements(By.CLASS_NAME, 'q-td.q-column--txDate')
        self.tradeSizes = self.driver.find_elements(By.CLASS_NAME, "q-field.trade-size")
        self.tradeLinks = self.driver.find_elements(By.CLASS_NAME, "entity-link.entity-transaction.more-link")
        return len(self.tradeNames) #num of trades 
    
    ###  Gets specifics of each page, formats and outputs as Trade object
    ###
    def _getSpecifics(self, i) -> Trade:
        link = str(self.tradeLinks[i].get_attribute('href'))
        lastName = self.tradeNames[i].text.split(' ')[-1].strip()
        firstName = self.tradeNames[i].text.split(' ')[0].strip()
        #link = self.tradeLinks[i].get_attribute('href')
        date = self.tradeDates[i].text.replace('\n', ' ')
        date = date.split()
        date = dt.datetime(year=int(date[0]),month=self.months[date[2]], day=int(date[1]) )
        date = date.strftime("%m-%d-%Y")
        ticker = self.tradeTickers[i].text.split(":")[0]
        type = self.tradeTypes[i].text
        size = self.tradeSizes[i].text
        try:
            country = self.tradeTickers[i].text.split(":")[1]
        except:
            country = 'N/A'
        trade = Trade(firstName,lastName, date, ticker, type, country, link, size)
        return trade
    
    def getPageInfo(self) -> list:
        tradeList = []
        numTrades = self._getListsPerPage(self.url)
        for i in range(numTrades):
            tradeList.append(self._getSpecifics(i))
        return tradeList

        

class Scraper():
    def __init__(self, pages, byWhat=False) -> None:
        self.pages = pages
        self.byPubDate='https://www.capitoltrades.com/trades?sortBy=-pubDate&page={}'
        self.byTradeDate = 'https://www.capitoltrades.com/trades?sortBy=-txDate&page={}'
        ## true = by publication date, false = sort by trade date
        if byWhat:
            self.url = self.byPubDate
        else:
            self.url=self.byTradeDate
        self.tradeList = TradeList()
        self.tickers = Tickers.getTickers() ###dictionary of ticker:industry


    
    def scrape(self) -> None:
        # Create ChromeOptions object
        chrome_options = Options()

        # Set headless mode
        chrome_options.add_argument("--headless=new")   
        driver = webdriver.Chrome()        
        
        for i in range(1, self.pages): 
            url = self.url.format(i)
            page = Page(url, driver)
            pageInfo = page.getPageInfo()
            self.tradeList.extendTrades(pageInfo)