from pymongo import MongoClient
from models import DialogItem
import pymongo
from bson.objectid import ObjectId

class MongoService:
    itemsPerPage = 30
    
    def __init__(self, connectionString: str = "mongodb://admin:password@localhost:27017"):
        client = MongoClient(connectionString)
        self.client = client
        self.db = client.chatbot
        self.dialogItems = self.db.dialogItems

    def get(self, customerId: str = None, language: str = None, bookmark: str = None):
        # Paginate by providing the id of the last item on the previous page
        #
        # Returns: [dialogItems, bookmark]
        #   dialogItems: Any found dialog items
        #   bookmark: The bookmark to use to get the next page
        #
        query = {}
        if customerId is not None:
            query.update({"customerId": customerId})
        if language is not None:
            query.update({"language": language})            
        if bookmark is not None:
            query.update({"_id": {"$gt": ObjectId(bookmark)}})
        
        results = list(self.dialogItems.find(query).limit(self.itemsPerPage).sort("_id", pymongo.ASCENDING))
        dialogItems = list(map(lambda dialogItem: \
            DialogItem(dialogItem["customerId"], dialogItem["dialogId"], dialogItem["text"], dialogItem["language"]), \
            results))
        
        bookmark = None
        if dialogItems:
            bookmark = str(results[-1]["_id"])
        
        return dialogItems, bookmark
    
    def insert(self, dialogItem: DialogItem):
        # Inserts the provided dialogItem into the database
        return self.dialogItems.insert_one(dialogItem)
