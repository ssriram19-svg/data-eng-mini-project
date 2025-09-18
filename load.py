import pandas as pd

def load():
    df = pd.read_csv("data/transformed.csv")
    # Simulate loading into Snowflake warehouse
    df.to_csv("data/warehouse.csv", index=False)
    return df

if __name__ == "__main__":
    load()
