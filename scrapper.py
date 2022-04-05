

from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen
from WikiRoute import Route

class ScrapperUtils:

    def _ParseSingleRoute_(self, route, raw_item):
        """
        Given a raw_item route element from wikiloc, parse all
        fields in the route and returns a Route element
        """
        route = Route()
        c = raw_item.contents[1]

        route.name          = c.contents[1].contents[1].text.strip()
        route.activity      = c.contents[1].contents[3].contents[3].text.strip()
        route.start         = c.contents[3].text.strip()
        route.distance      = c.contents[5].contents[3].contents[1].contents[3].text
        route.elevation     = c.contents[5].contents[3].contents[3].contents[3].text
        rank                = c.contents[5].contents[3].contents[5].contents[3].text.strip().split('|')    
        route.rank1         = rank[0].strip()
        route.rank2         = rank[1].strip()
        route.imageUrl1      = c.contents[7].contents[1].contents[1].attrs['srcset']
        route.imageUrl2      = c.contents[7].contents[3].contents[1].attrs['srcset']
        route.imageUrl3      = c.contents[7].contents[5].contents[1].attrs['srcset']

        return route

    def ParseRoutesPage(self, url, ItemsList):
        """
        Parses all available routes in a URL page
        """
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

        # Initialize the soup reader and read the full webpage
        webpage = urlopen(req).read()
        soup = bs(webpage,'html.parser')

        # Find items under <ul class> tag
        items = soup.find('ul')
        list_items = items.contents

        for j in range(1, len(list_items) - 1):
            # Parse each item
            newRoute = Route()
            ItemsList.append(self._ParseSingleRoute_(newRoute, list_items[j]))


    









