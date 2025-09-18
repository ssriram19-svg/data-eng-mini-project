import pandas as pd

def transform():
    # Read from the file created by extract.py
    df = pd.read_csv("data/extracted.csv")

    # Simple transformation: select only name and country
    df = df[["name", "country"]]

    # Write transformed output
    df.to_csv("data/transformed.csv", index=False)

if __name__ == "__main__":
    transform()
