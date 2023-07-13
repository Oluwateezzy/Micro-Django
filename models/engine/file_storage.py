import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def save(self):
        data = {}
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            # new_obj = {key:value.to_dict() for key, value in FileStorage.__objects.items()}
            for key, value in self.__objects.items():
              data[key] = value.to_dict()
            json.dump(data, file)

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    cls_name, cls_id = key.split(".")
                    cls = eval(cls_name)
                    FileStorage.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
