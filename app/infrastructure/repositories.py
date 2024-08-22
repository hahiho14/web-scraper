import pandas as pd

class ArticleRepository:
    """A repository class for handling article data storage."""
    def save_to_csv(self, data, file_path: str):
        """Saves the scraped article data to a CSV file.

        Args:
            data (list): A list of dictionaries containing article data.
            file_path (str): The file path where the CSV should be saved.
        """
        df = pd.DataFrame(data)
        df.to_csv(file_path, index=False)
