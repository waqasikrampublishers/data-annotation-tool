import re

def preprocess_data(data):
    # Remove special characters and extra whitespace
    data = re.sub(r'[^\w\s]', '', data)
    data = re.sub(r'\s+', ' ', data)
    return data
