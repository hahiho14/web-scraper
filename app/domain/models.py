from typing import Optional

class Article:
    def __init__(self, id: int, title: str, subtitle: str, content: str, date: str):
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.content = content
        self.date = date
