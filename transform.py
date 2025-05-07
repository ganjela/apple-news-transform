from pandas import json_normalize
import pandas as pd
pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns',50)
pd.set_option('display.width', 50)
pd.set_option('display.max_colwidth', 50)
class Transformer:
     def __init__(self, data):
         self.df = json_normalize(data)

     def transform(self):
        self.df.dropna(subset=["author"], inplace=True)
        self.df.drop(columns=["source.id"], inplace=True)

        self.df.rename(columns={"source.name": "source_name"}, inplace=True)
        self.df.rename(columns={"urlToImage": "url_to_image"}, inplace=True)
        self.df.rename(columns={"publishedAt": "published_at"}, inplace=True)

        self.df['title'] = self.df["title"].replace(to_replace = r"[\r\n]", value = '', regex=True)
        self.df['description'] = self.df["description"].replace(to_replace = r"[\r\n]", value = '', regex=True)
        self.df['content'] = self.df["content"].replace(to_replace=r"[\r\n]", value='', regex=True)

        self.df["published_at"] = pd.to_datetime(self.df["published_at"])

        return self.df
