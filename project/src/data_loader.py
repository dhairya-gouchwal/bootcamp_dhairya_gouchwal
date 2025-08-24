import pandas as pd

def load_prices(file_path: str) -> pd.DataFrame:
    """Load historical prices CSV with Date as index"""
    df = pd.read_csv(file_path, parse_dates=["Date"], index_col="Date")
    return df

def load_credit(file_path: str) -> pd.DataFrame:
    """Load credit data (PD, LGD, EAD)"""
    return pd.read_csv(file_path)