from pandas import json_normalize

class Transformer:
     def __init__(self, data):
         self.df = json_normalize(data)

     def transform(self):
        self.df.dropna(subset=["author"], inplace=True)
        self.df.drop(columns=["source.id"], inplace=True)

        self.df.rename(columns={"source.name": "source"}, inplace=True)

        self.df['title'] = self.df["title"].replace(to_replace = r"[\r\n]", value = '', regex=True)
        self.df['description'] = self.df["description"].replace(to_replace = r"[\r\n]", value = '', regex=True)

        return self.df
