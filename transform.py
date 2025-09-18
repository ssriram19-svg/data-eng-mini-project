import pandas as pd

def transform():
    df = pd.read_csv("data/extracted.csv")
    # Trim whitespace in names
    df["name"] = df["name"].str.strip()
    # Add a column with 10% tax
    df["purchase_with_tax"] = df["purchase"] * 1.1
    df.to_csv("data/transformed.csv", index=False)
    return df

if __name__ == "__main__":
    transform()
