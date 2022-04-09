
from scrapper import ScrapperUtils
from exporter import CsvExporter

# Initialize the final Item List
ItemsList = []

# Initialize the ScrapperUtils class with used methods
# for scrapping
utils = ScrapperUtils()
exporter = CsvExporter()

# Initialize web scrapping on defined URL
for i in range(1, 100, 1):
    url = "https://ca.wikiloc.com/rutes/senderisme/espanya/catalunya?page=" + str(i)
    utils.ParseRoutesPage(url, ItemsList)

# Export to csv to custom path
exporter.ToCsv(ItemsList, 'data.csv')

