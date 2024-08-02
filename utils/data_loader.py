import pandas as pd

# Helper function to load data from a CSV file and preprocess it
def load_data(file_path):
    data = pd.read_csv(file_path)
    # Convert the 'Date' column to datetime format
    data['Date'] = pd.to_datetime(data['Date'])
    return data
