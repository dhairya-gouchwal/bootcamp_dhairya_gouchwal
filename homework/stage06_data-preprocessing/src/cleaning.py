#Cleaning data 
#to do 
# df = cleaning.fill_missing_median(df, ['col1','col2'])
# df = cleaning.drop_missing(df, threshold=0.5)
# df = cleaning.normalize_data(df, ['col1','col2'])

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def fill_missing_median(df : pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        df[col] = df[col].fillna(df[col].median())
    return df

def drop_missing(df: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    
    df = df.copy()
    return df.loc[:, df.isnull().mean() < threshold]

def normalize_data(df: pd.DataFrame) -> pd.DataFrame:
    
    df = df.copy()
    scaler = MinMaxScaler()
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    return df

