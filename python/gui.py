'''
Class handles user input
'''


class Gui():
    def __init__(self) -> None:
        pass    
    def getInput(self) -> (int, bool):
        pages = int(input("How many pages of stocks? "))
        byWhat = input("To sort by publication date enter 'y'. To sort by Trade date enter 'n'. ")
        ### each instance of scraper creates its own instance of TradeList
        ### byWhat: True=find by publication date, False= find by trade date
        while byWhat != 'y' and byWhat != 'n':
            byWhat = input("Please enter 'y' or 'n': ")
        byPubDate = False
        if byWhat == 'y':
            byPubDate = True

        return pages, byPubDate

    def getFilepath(self) -> str:
        filename = input("What would you like to name your Excel sheet? (Do not include file extension)  ")
        filename = filename + '.xlsx'
        return filename
    