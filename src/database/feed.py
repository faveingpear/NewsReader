from database.item import item

class feed():

    items = []
    id = None
    url = None
    title = None
    faviconLink = None
    added = None
    folderId = None
    unreadCount = None
    ordering = None
    link = None
    pinned = None
    newestItemId = None

    def setItems(self,items):
        self.items = items

    def setId(self, id):
        self.id = id

    def setUrl(self, url):
        self.url = url
    
    def setTitle(self, title):
        self.title = title

    def setFaviconLink(self, faviconLink):
        self.faviconLink = faviconLink
    
    def setAdded(self, added):
        self.added = added

    def setFolderId(self, folderId):
        self.folderId = folderId

    def setUnreadCount(self, unreadCount):
        self.unreadCount = unreadCount

    def setOrdering(self, ordering):
        self.ordering = ordering

    def setLink(self, link):
        self.link = link

    def setPinned(self, pinned):
        self.pinned = pinned
    
    def setNewestItemId(self, newestItemId):
        self.newestItemId = newestItemId

    def getId(self):
        return self.id

    def getUrl(self):
        return self.url

    def getTitle(self):
        return self.title
    
    def getFaviconLink(self):
        return self.faviconLink
    
    def getAdded(self):
        return self.added
    
    def getFolderId(self):
        return self.folderId
    
    def getUnreadCount(self):
        return self.unreadCount
    
    def getOrdering(self):
        return self.ordering
    
    def getLink(self):
        return self.link
    
    def getPinned(self):
        return self.pinned
    
    def getNewestItemId(self):
        return self.newestItemId
    
    def getItems(self):
        return self.items

    def addItem(self, item: item):
        self.items.append(item)