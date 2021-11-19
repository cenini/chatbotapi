from abc import ABC, abstractmethod
from models import DialogItem

class StorageProvider(ABC):
    @abstractmethod
    def get(self, customerId: str = None, language: str = None, bookmark: str = None):
        pass
    
    @abstractmethod
    def insert(self, dialogItem: DialogItem):
        pass
    
    @abstractmethod
    def delete_customer_dialogs(self, customerId):
        pass
    
    