from mongo_service import MongoService
from models import DialogItem
import uuid
import os

class MongoDatabasePopulator:
    def populate(self, numberOfCustomers: int = 15, dialogLength: int = 10):
        languages = ["EN", "DE"]

        mongoService = MongoService(os.environ["MONGO_CONNECTION_STRING"])

        for customer in range(numberOfCustomers):
            customerId = str(uuid.uuid1())
            dialogId = str(uuid.uuid1())
            for index in range(dialogLength):
                dialogItem = DialogItem(customerId, dialogId, "text" + str(index), languages[index%2])
                mongoService.insert(dialogItem)
    