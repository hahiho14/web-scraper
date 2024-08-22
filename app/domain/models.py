class Article:
    """Represents an article with its details.

    Attributes:
        id (int): The unique identifier for the article.
        title (str): The title of the article.
        subtitle (str): The subtitle of the article.
        content (str): The content of the article.
        date (str): The publication date of the article.
    """
    def __init__(self, id: int, title: str, subtitle: str, content: str, date: str):
        """Initializes an Article instance with the given details.

        Args:
            id (int): The unique identifier for the article.
            title (str): The title of the article.
            subtitle (str): The subtitle of the article.
            content (str): The content of the article.
            date (str): The publication date of the article.
        """
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.content = content
        self.date = date
