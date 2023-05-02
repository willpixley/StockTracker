# StockTracker
StockTracker uses Python and Selenium Webscraping to track stock trades by members of Congress, calculate their success, and return a spreadsheet of the trades. StockTracker pulls trade data from www.capitoltrades.com and stock history data from Yahoo Finance. Click on each trade's respective link to get more trade-specific information. When a trade is colored red, it means that there is overlap between the GICS sector of the stock and the committees that the member of congress are on.

Modules to install:
Pandas, yfinance, selenium, webdriver-manager, chromedriver-py, chromedriver, styleframe

All of these modules can be installed via pip using the names above. All other modules used in the program should be installed by default when you install Python.

Don't hesitate to email me with questions, suggestions, or concerns @ wtpixley@gmail.com

# Setup

To run, open in an IDE and run the main.py file. StockTrader should independently download all required packages, however if you'd like to see what it's downloading, check out the requirements.txt file. It will prompt you to enter the number of pages of stocks you'd like to look at. It will then ask if you'd like to examine trades by publication date or trade date. Examining by trade date will return the most recent trades and is recommended. After scraping the necessary trade data and downloading stock historical data, it will ask what you'd like to name your Excel sheet. After naming your sheet it will save it in the same folder as main.py.
