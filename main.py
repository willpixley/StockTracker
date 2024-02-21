from python.compare import Compare
from python.gui import Gui



def main():
    #subprocess.check_call(['pip', 'install', '--user', '-r', 'requirements.txt']) ### downloads required modules
    gui = Gui()
    pages, byPubDate = gui.getInput()
    
    c = Compare(pages, byWhat=byPubDate)
    c.findOverlap()
    c.findGoodTrades()
    filename = 'output/'+gui.getFilepath()
    c.storable.toExcel(filename)


if __name__ == '__main__':
    main()

