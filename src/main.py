from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

class DialogItem(BaseModel):
    text: str
    language: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/data/{customerId}/{dialogId}")
def push_dialog(customerId: str, dialogId: str, dialogItem: DialogItem):
    return {"method": "post", "customerId": customerId, "dialogId": dialogId, "item_text": dialogItem.text, "item_language": dialogItem.language}

@app.post("/consents/{dialogId}")
def push_consent(dialogId: str, consent: str = Body(...)):
    return {"method": "post", "dialogId": dialogId, "consent": consent}