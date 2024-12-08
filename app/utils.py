import pandas as pd

def load_data(filepath):
    #Load and preprocess the dataset.
    try:
        data = pd.read_csv(filepath)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")
