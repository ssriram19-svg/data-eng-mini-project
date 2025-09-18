import pandas as pd

def transform():
    # Read extracted data
    df = pd.read_csv("data/oracle_customers.csv")  # or extracted.csv if that’s your file

    # Simple transformation: keep only name + country
    df = df[["name", "country"]]

    # Save transformed file
    df.to_csv("data/transformed.csv", index=False)

if __name__ == "__main__":
    transform()
