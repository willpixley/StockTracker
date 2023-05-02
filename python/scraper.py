from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime as dt
import python.Tickers as Tickers
from python.TradeList import TradeList
from python.trade import Trade


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
        self.tickers = Tickers.getTickers() ###dictionary of ticker:industry
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