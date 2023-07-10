from uuid import uuid4
import datetime
from models import storage


class BaseModel:
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at":
                    value = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    value = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if "id" not in kwargs.keys():
                    self.id = uuid4()
                if "created_at" not in kwargs.keys():
                    self.created_at = datetime.datetime.now()
                if "updated_at" not in kwargs.keys():
                    self.updated_at = datetime.datetime.now()
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self) -> str:
        class_name = self.__class__.__name__
        return f"[{class_name}] [{self.id}] {self.__dict__}"

    def save(self):
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        class_name = self.__class__.__name__
        obj = self.__dict__.copy()
        obj["created_at"] = self.created_at.isoformat()
        obj["updated_at"] = self.updated_at.isoformat()
        return obj
