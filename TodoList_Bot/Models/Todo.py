class Todo:
    def __init__(self, title, is_completed=False):
        self.title = title
        self.is_completed = is_completed

    def set_completed(self):
        self.is_completed = True
