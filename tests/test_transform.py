import pandas as pd

def test_transform_columns():
    df = pd.read_csv("data/transformed.csv")
    assert "purchase_with_tax" in df.columns
