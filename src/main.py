from typing import Optional
from fastapi import Body, FastAPI
from models import ChatItem, DialogItem
from mongo_service import MongoService
from distutils import util
import uvicorn

chatbotapi = FastAPI()
connectionString = "mongodb://root:apassword@mongo:27017"
storageProvider = MongoService(connectionString)

@chatbotapi.post("/data/{customerId}/{dialogId}")
async def push_dialog(customerId: str, dialogId: str, chatItem: ChatItem):
    acknowledged = storageProvider.insert(DialogItem(customerId, dialogId, chatItem.text, chatItem.language))
    return {"acknowledged": acknowledged}

@chatbotapi.post("/consents/{dialogId}")
async def push_consent(dialogId: str, consent: str = Body(None, regex="^true$|^false$")):
    acknowledged = True
    if (not util.strtobool(consent)):
        acknowledged = storageProvider.delete_customer_dialogs(dialogId)
    return {"acknowledged": acknowledged}

@chatbotapi.get("/data/")
async def read_dialogs(language: Optional[str] = None, customerId: Optional[str] = None, bookmark: Optional[str] = None):
    results, bookmark = storageProvider.get(customerId, language, bookmark)
    return {"results": results, "bookmark": bookmark}

if __name__ == "__main__":
    uvicorn.run(chatbotapi, host="0.0.0.0", port=8000)