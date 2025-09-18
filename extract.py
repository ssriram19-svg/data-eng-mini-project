import pandas as pd
import os

def extract():
    os.makedirs("data", exist_ok=True)  # make sure 'data' folder exists
    data = {
        "id": [1, 2, 3],
        "name": ["Alice ", " Bob", "Charlie"],
        "purchase": [120, 250, 300]
    }
    df = pd.DataFrame(data)
    df.to_csv("data/extracted.csv", index=False)
    return df

if __name__ == "__main__":
    extract()
# this code is for extracting the data and storing it in CSV
