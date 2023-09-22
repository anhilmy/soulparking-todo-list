from datetime import datetime

from error.error import ValidationError


class TodoListModel:
    __next_id = 1
    __data = []

    # instance method
    def __init__(self, id, title, description):
        self.id = id
        # other opt: generateUUID

        self.title = title
        self.description = description
        self.created_at = datetime.now()

    def done(self):
        self.updated_at = datetime.now()
        self.finished_at = datetime.now()

    def delete(self):
        self.deleted_at = datetime.now()

    def update(self, title=None, description=None):
        self.updated_at = datetime.now()
        if title:
            self.title = title
        if description:
            self.description = description

    def detail(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "created_at": self.created_at,
            "finished_at": getattr(self, "finished_at", None),
            "updated_at": getattr(self, "updated_at", None),
            "deleted_at": getattr(self, "deleted_at", None),
        }

    # class method
    @classmethod
    def get_by_id(cls, id):
        for instance in cls.__data:
            if id == instance.id:
                return instance
        return None

    @classmethod
    def get_all(cls, is_active=True):
        if is_active:
            res = []
            for instance in cls.__data:
                if not hasattr(instance, "deleted_at"):
                    res.append(instance)
            return res

        return cls.__data

    @classmethod
    def create(cls, title, description):
        id = cls.__next_id
        cls.__next_id += 1

        new_todo = TodoListModel(id, title, description)
        cls.__data.append(new_todo)
        return new_todo

    @staticmethod
    def validate(title, description):
        if title is None or len(title) == 0:
            raise ValidationError("title is required")
        return None
