from pydantic import BaseModel

class ChatItem(BaseModel):
    text: str
    language: str
    
class DialogItem():
    customerId: str
    dialogId: str
    text: str
    language: str

    def __init__(self, customerId: str, dialogId: str, text: str, language: str):
        self.customerId = customerId
        self.dialogId = dialogId
        self.text = text
        self.language = language