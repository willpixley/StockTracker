import subprocess
from python.compare import Compare



def main():
    #subprocess.check_call(['pip', 'install', '--user', '-r', 'requirements.txt']) ### downloads required modules
    pages = int(input("How many pages of stocks? "))
    byWhat = input("To sort by publication date enter 'y'. To sort by Trade date enter 'n'. ")
    ### each instance of scraper creates its own instance of TradeList
    ### byWhat: True=find by publication date, False= find by trade date
    while byWhat != 'y' and byWhat != 'n':
        byWhat = input("Please enter 'y' or 'n': ")
    status = False
    if byWhat == 'y':
        status = True
    
    c = Compare(pages, byWhat=status)
    c.findOverlap()
    c.findGoodTrades()
    filename = input("What would you like to name your Excel sheet? (Do not include file extension)  ")
    filename = filename + '.xlsx'
    c.storable.toExcel(filename)


if __name__ == '__main__':
    main()

