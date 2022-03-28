class Route(object):
    """
    Defines the available parameters in a Wikiloc Route objects.
    """
    
    def __init__(self, name=None, activity=none, start=None, distance=0.0, elevation=0.0, rank1=0.0, rank2=0.0, description=None):
        """
        Instantiate an Article
        :param name: name of the article
        :param price: price of the article
        :param no_iva: price without IVA of the article
        :param pvp: PVP price of the article
        :param discount: discount applied
        :param rating: rating of the article
        :param features: list of article's features: see feature.py
        """
        self.name = name
        self.activity = activity
        self.start = start
        self.distance = distance
        self.elevation = elevation
        self.rank1 = rank1
        self.rank2 = rank2
        self.description = description
