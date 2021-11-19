from pymongo import MongoClient
from models import DialogItem
from storage_provider import StorageProvider
import pymongo
from bson.objectid import ObjectId

class MongoService(StorageProvider):
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
        result = self.dialogItems.insert_one(dialogItem.__dict__)
        return result.acknowledged

    def delete_customer_dialogs(self, dialogId):
        # Deletes all dialogItems for the customer having the
        # provided dialog
        customerResult = list(self.dialogItems.find({"dialogId": dialogId}).limit(1))
        if (len(customerResult) > 0):
            query = {"customerId": customerResult[0]["customerId"]}
            deleteResult = self.dialogItems.delete_many(query)
            return deleteResult.acknowledged
        
        return False