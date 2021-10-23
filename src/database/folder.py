from database.feed import feed
from database.item import item

class folder():

    id = None
    feeds = []
    name = None
    
    def __init__(self, id,feeds = [], name = None) -> None:
        self.id = id
        self.feeds = []
        self.name = name

    def setId(self, id:int):
        self.id = id

    def setFeeds(self, feeds):
        self.feeds = feeds
    
    def setName(self, name):
        self.name = name

    def getId(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getFeeds(self) -> feed:
        return self.feeds
    
    def getId(self):
        return self.id

    def addFeed(self, feed: feed):
        self.feeds.append(feed)