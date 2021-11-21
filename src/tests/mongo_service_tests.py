import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import unittest
from models import DialogItem
from mongo_service import MongoService
import uuid

class MongoServiceTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.mongoService = MongoService(os.environ["MONGO_CONNECTION_STRING"])
        
    def test_insert(self):
        id = str(uuid.uuid1())
        
        acknowledged = self.mongoService.insert(DialogItem(id, id, "text", "EN"))
        
        self.assertTrue(acknowledged)
                                 
    def test_get(self):
        result, bookmark = self.mongoService.get()
        
        self.assertNotEqual(len(result), 0)
        self.assertIsNotNone(bookmark)
        
    def test_getting_inserted_dialog_for_customer(self):
        id = str(uuid.uuid1())
        
        self.mongoService.insert(DialogItem(id, id, "text", "EN"))
        self.mongoService.insert(DialogItem(id, id, "other text", "EN"))
        result, bookmark = self.mongoService.get(customerId=id) 
        
        self.assertTrue(all(dialogItem.customerId == id for dialogItem in result))
        self.assertTrue(len(result) == 2)
        
    def test_get_with_english_language(self):
        language = "EN"
        
        result, bookmark = self.mongoService.get(language=language)
        
        self.assertTrue(all(dialogItem.language == language for dialogItem in result))
        self.assertTrue(len(result) > 0)
        self.assertIsNotNone(bookmark)
        
    def test_get_with_german_language(self):
        language = "DE"
        
        result, bookmark = self.mongoService.get(language=language)
        
        self.assertTrue(all(dialogItem.language == language for dialogItem in result))
        self.assertTrue(len(result) > 0)
        self.assertIsNotNone(bookmark)
        
    def test_deleting_dialogs_for_customer(self):
        customerId = str(uuid.uuid1())
        dialogId1 = str(uuid.uuid1())
        dialogId2 = str(uuid.uuid1())
        self.mongoService.insert(DialogItem(customerId, dialogId1, "text", "EN"))
        self.mongoService.insert(DialogItem(customerId, dialogId1, "other text", "EN"))
        self.mongoService.insert(DialogItem(customerId, dialogId2, "next dialog", "EN"))  
              
        deleteAcknowledged = self.mongoService.delete_customer_dialogs(dialogId1) 
        getResult, bookmark = self.mongoService.get(customerId=customerId)
        
        self.assertTrue(deleteAcknowledged)
        self.assertTrue(len(getResult) == 0)
        
if __name__ == '__main__':
    unittest.main()