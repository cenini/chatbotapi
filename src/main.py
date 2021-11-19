from typing import Optional
from fastapi import Body, FastAPI
from models import ChatItem

app = FastAPI()

@app.post("/data/{customerId}/{dialogId}")
async def push_dialog(customerId: str, dialogId: str, chatItem: ChatItem):
    return {"method": "post", "customerId": customerId, "dialogId": dialogId, "item_text": chatItem.text, "item_language": chatItem.language}

@app.post("/consents/{dialogId}")
async def push_consent(dialogId: str, consent: str = Body(None, regex="^true$|^false$")):
    return {"method": "post", "dialogId": dialogId, "consent": consent}

@app.get("/data/")
async def read_items(language: Optional[str] = None, customerId: Optional[str] = None):
    results = {}
    if language:
        results.update({"language": language})
    if customerId:
        results.update({"customerId": customerId})
    return results