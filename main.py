from python.compare import Compare
from python.gui import Gui
import os


def main():
    #subprocess.check_call(['pip', 'install', '--user', '-r', 'requirements.txt']) ### downloads required modules
    gui = Gui()
    pages, byPubDate = gui.getInput()
    
    c = Compare(pages, byWhat=byPubDate)
    c.findOverlap()
    c.findGoodTrades()
    if not os.path.exists('output'):
    # If the directory doesn't exist, create it
        os.makedirs('output')
    filename = 'output/'+gui.getFilepath()
    c.storable.toExcel(filename)


if __name__ == '__main__':
    main()

