import pandas as pd

class ArticleRepository:
    def save_to_csv(self, data, file_path: str):
        df = pd.DataFrame(data)
        df.to_csv(file_path, index=False)
