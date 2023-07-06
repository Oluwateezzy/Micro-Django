from uuid import uuid4
import datetime


class BaseModel:
    def __init__(self) -> None:
        self.id = str(uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self) -> str:
        class_name = self.__class__.__name__
        return f"[{class_name}] [{self.id}] {self.__dict__}"

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        class_name = self.__class__.__name__
        obj = self.__dict__.copy()
        obj["created_at"] = self.created_at.isoformat()
        obj["updated_at"] = self.updated_at.isoformat()
        return obj
