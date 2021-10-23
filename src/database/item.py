
# TODO: Add type checking 
# TODO: sanitize title and body maybe?

class item():

    id = None
    guid = None
    guidHash = None
    url = None
    title = None
    author = None
    pubDate = None #?
    body = None
    enclosureMime = None
    enclosureLink = None
    mediaThumbnail = None
    mediaDesciption = None
    feedId = None
    unread = None
    starred = None
    rtl = None
    lastModified = None
    fingerprint = None

    def __init__(self) -> None:
        pass

    def setId(self,itemId):
        self.id = itemId

    def setGuid(self, guid):
        self.guid = guid

    def setGuidHash(self, guidHash):
        self.guidHash = guidHash

    def setUrl(self, url):
        self.url = url

    def setTitle(self, title):
        self.title = title

    def setAuthor(self, author):
        self.author = author

    def setPubDate(self, pubDate):
        self.pubDate = pubDate

    def setBody(self, body):
        self.body = body

    def setEnclosureMime(self, enclosureMime):
        self.enclosureMime = enclosureMime

    def setEnclosureLink(self, enclosureLink):
        self.enclosureLink = enclosureLink

    def setMediaThumbnail(self, mediaThumbail):
        self.mediaThumbnail = mediaThumbail

    def setMediaDescription(self, mediaDescription):
        self.mediaDesciption = mediaDescription

    def setFeedId(self, feeId):
        self.feedId = feeId

    def setUnread(self, unread):
        self.unread = unread

    def setStarred(self, starred):
        self.starred = starred

    def setRtl(self, rtl):
        self.rtl = rtl

    def setLastModified(self, lastModified):
        self.lastModified = lastModified

    def setFingerPrint(self, fingerPrint):
        self.fingerprint = fingerPrint

    def getId(self):
        return self.id

    def getGuid(self):
        return self.guid
    
    def getGuidHash(self):
        return self.guidHash

    def getUrl(self):
        return self.url

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author

    def getPubDate(self):
        return self.pubDate

    def getBody(self):
        return self.body

    def getEnclosureMime(self):
        return self.enclosureLink

    def getEnclosureLink(self):
        return self.enclosureLink

    def getMediaThumbnail(self):
        return self.mediaThumbnail

    def getMediaDesciption(self):
        return self.mediaDesciption

    def getFeedId(self):
        return self.feedId

    def getUnread(self):
        return self.unread

    def getStarred(self):
        return self.starred

    def getRtl(self):
        return self.rtl

    def getLastModified(self):
        return self.lastModified

    def getFingerprint(self):
        return self.fingerprint