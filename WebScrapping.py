

from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen
from WikiRoute import Route

def ParseSingleRoute(route, raw_item):

    route = Route()

    c = raw_item.contents[1]

    route.name = c.contents[1].contents[1].text.strip()
    route.activity = c.contents[1].contents[3].text.strip()
    route.near = c.contents[3].text.strip()
    route.distance = c.contents[5].contents[3].contents[1].contents[3].text
    route.elevation = c.contents[5].contents[3].contents[3].contents[3].text
    rank = c.contents[5].contents[3].contents[5].contents[3].text.strip().split('|')    
    route.rank1 = rank[0].strip()
    route.rank2 = rank[1].strip()
    route.descr = c.contents[9].text.strip()

    return route


# Initialize the request for the web page
# By default, 25 items will be load for each page. If want to get 25 more items,
# just use the next URL's https://ca.wikiloc.com/rutes/senderisme/espanya/catalunya?page=3
req = Request('https://ca.wikiloc.com/rutes/senderisme/espanya/catalunya', headers={'User-Agent': 'Mozilla/5.0'})
# req = Request('https://ca.wikiloc.com/rutes/senderisme/espanya/catalunya?page=2', headers={'User-Agent': 'Mozilla/5.0'})
# req = Request('https://ca.wikiloc.com/rutes/senderisme/espanya/catalunya?page=3', headers={'User-Agent': 'Mozilla/5.0'})
# req = Request('https://ca.wikiloc.com/rutes/senderisme/espanya/catalunya?page=4', headers={'User-Agent': 'Mozilla/5.0'})
# req = Request('https://ca.wikiloc.com/rutes/senderisme/espanya/catalunya?page=5', headers={'User-Agent': 'Mozilla/5.0'})
# req = Request('https://ca.wikiloc.com/rutes/senderisme/espanya/catalunya?page=6', headers={'User-Agent': 'Mozilla/5.0'})
# req = Request('https://ca.wikiloc.com/rutes/senderisme/espanya/catalunya?page=7', headers={'User-Agent': 'Mozilla/5.0'})
# req = Request('https://ca.wikiloc.com/rutes/senderisme/espanya/catalunya?page=8', headers={'User-Agent': 'Mozilla/5.0'})
# req = Request('https://ca.wikiloc.com/rutes/senderisme/espanya/catalunya?page=9', headers={'User-Agent': 'Mozilla/5.0'})


# Initialize the soup reader and read the full webpage
webpage = urlopen(req).read()
soup = bs(webpage,'html.parser')

# Find items under <ul class> tag
items = soup.find('ul')
list_items = items.contents

# Parse each item in the list_items
ItemsList = []

for i in range(1, len(list_items) - 1):
    # Parse each item
    ItemsList.append(ParseItem(list_items[i]))
    

print(ItemsList)
print(len(ItemsList))



#for raw_item in list_items:
#    # Parse each 
    









