from database.feed import feed
from database.folder import folder
from database.item import item

import logging

class database():

    folders = []
    lastModified = None
    lastUpdated = None

    def __init__(self) -> None:
        pass

    def parseJson(self, data):
        pass

    # def addFolder(self, folderObject: folder):

    #     if folderObject.getId() == None:
    #         logging.error("FolderObject does not contain a id")
    #         raise Exception("Folders must contain a id")
    #     else:
    #         self.folders.append(folderObject)

    def addFolder(self, id, feeds = [], name = None):

        self.folders.append(folder(
            id=id,
            feeds=feeds,
            name=name
        ))

        logging.info("databse: Added folder:" + str(id))

    def addFeed(self, feedObject: feed):

        if feedObject.id == None:
            logging.error("feedObject does not contain a id")
            raise Exception("Feed must contain a id")
        else:
            try:
                self.searchForFolder(feedObject.getId()).addFeed(feed)
            except:
                pass
                
    def addItem(self, itemObject):
        if item.getId() == None:
            logging.error("feedObject does not contain a id")
            raise Exception("Feed must contain a id")
        else:
            try:
                feed = self.searchForFeed(itemObject.getFeedId())
                feed.addItem(item)
            except:
                pass


    def getFolder(self, folderid):
        pass

    def getAllFolders(self):
        return self.folders

    def getFeed(self,feedId):
        pass

    def getItem(self, itemId):
        pass

    def removeFolder(self, folderId):
        pass

    def removeFeed(self, feedId):
        pass

    def removeItem(self, itemId):
        pass

    def markItemread(itemid):
        pass

    def markItemStarred(itemId):
        pass

    def saveDatabase():
        pass

    def loadDatabase():
        pass

    def searchForFolder(self, folderId: int) -> folder:
        for folder in self.folders:
            if folder.getId() == folderId:
                return folder
            else:
                raise Exception("Folder not found")

    def searchForFeed(self, feedId: int) -> feed:
        for folder in self.folders:
            for feed in folder.getFeeds():
                if feed.getId() == feedId:
                    return feed
                else:
                    raise Exception("Feed not found")
    
    def searchForItem(self, itemId:int) -> item:
        for folder in self.folders:
            for feed in folder.getFeeds():
                for item in feed.getItems():
                    if item.getId() == itemId:
                        return feed
                    else:
                        raise Exception("Item not found")