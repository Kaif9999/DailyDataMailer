import pandas as pd

class DataCleaner:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        return pd.read_csv(self.file_path)

    def clean_data(self, df):
        df.drop_duplicates(inplace=True)
        df.fillna(method='ffill', inplace=True)
        return df

    def save_data(self, df, output_path):
        df.to_csv(output_path, index=False)

    def clean(self, output_path='cleaned_data.csv'):
        df = self.load_data()
        df = self.clean_data(df)
        self.save_data(df, output_path)
        print(f"Data cleaned and saved to {output_path}")
