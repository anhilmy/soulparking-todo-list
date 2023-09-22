from datetime import datetime

class TodoList:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.created_at = datetime.now()