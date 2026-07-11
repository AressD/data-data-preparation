import pandas as pd
from pathlib import Path


class Olist:
    def get_data(self):
        csv_path = Path("~/.workintech/olist/data/csv").expanduser()
        file_names = [path.name for path in csv_path.iterdir() if path.name.endswith('.csv')]
        key_names = [
            name.replace('.csv', '').replace('_dataset', '').replace('olist_', '')
            for name in file_names
        ]
        data = {}
        for key, name in zip(key_names, file_names):
            data[key] = pd.read_csv(csv_path / name)
        return data
