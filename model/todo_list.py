from datetime import datetime

from component.error import ValidationError


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

    def _format_attribute_time(self, attribute_name):
        if not hasattr(self, attribute_name):
            return None

        return getattr(self, attribute_name).strftime("%d-%m-%Y %H:%M:%S")

    def complete(self):
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
            "created_at": self._format_attribute_time("created_at"),
            "finished_at": self._format_attribute_time("finished_at"),
            "updated_at": self._format_attribute_time("updated_at"),
            "deleted_at": self._format_attribute_time("deleted_at"),
        }

    # class method
    @classmethod
    def get_by_id(cls, id):
        for instance in cls.__data:
            if id == instance.id and (not hasattr(instance, "deleted_at")):
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
