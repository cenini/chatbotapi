from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

class DialogItem(BaseModel):
    text: str
    language: str

@app.post("/data/{customerId}/{dialogId}")
async def push_dialog(customerId: str, dialogId: str, dialogItem: DialogItem):
    return {"method": "post", "customerId": customerId, "dialogId": dialogId, "item_text": dialogItem.text, "item_language": dialogItem.language}

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