class Route(object):
    """
    Defines the available parameters in a Wikiloc Route objects.
    """
    
    def __init__(self, name=None, activity=None, start=None, distance=0.0, elevation=0.0, rank1=0.0, rank2=0.0, 
                 description=None, imageUrl1=None, imageUrl2=None, imageUrl3=None):
        """
        Instantiate an Article
        :param name: name of the route
        :param activity: Type of activity
        :param start: Description of the starting point
        :param distance: distance of the route
        :param elevation: Elevation gain of the route
        :param rank1: Wikiloc rating of the route
        :param rank2: Users rating of the route
        """
        self.name = name
        self.activity = activity
        self.start = start
        self.distance = distance
        self.elevation = elevation
        self.rank1 = rank1
        self.rank2 = rank2
        self.description = description
        self.imageUrl1 = imageUrl1
        self.imageUrl2 = imageUrl2
        self.imageUrl3 = imageUrl3
