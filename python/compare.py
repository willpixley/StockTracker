from python.TradeList import TradeList
from python.scraper import Scraper
import python.Tickers as Tickers
from python.committees import *
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

senateAssignments = getSenateCommittee()
houseAssignments = getHouseCommittee()
congressmanByCommittee = senateAssignments | houseAssignments

class Compare():
    def __init__(self, pages, byWhat=False) -> None:
        self.tickers = Tickers.getTickers() ###dictionary of ticker:industry
        self.scraper = Scraper(pages, byWhat=byWhat)
        self.scraper.scrape()
        self.storable = self.scraper.tradeList
        self.tradeList = self.scraper.tradeList.getList()
        self.sus = TradeList()
    
    def findOverlap(self):
        print("full committees", len(fullCommittees))
        count = 0
        for trade in self.tradeList:
            ### list of committees the congressman is in
            try: 
                committees = congressmanByCommittee[trade.last]

            except: 
                count +=1
                continue
            relevantIndustry = set()
            for c in committees:
                try:    
                    
                    relevantIndustry.update(fullCommittees[c])
                except: continue
            if trade.getIndustry(self.tickers) in relevantIndustry: ### returns industry of the ticker
                print("yes")
                trade.flag = True 
        print(count)
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