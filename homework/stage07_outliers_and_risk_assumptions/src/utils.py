import pandas as pd
#(a) detect_outliers_iqr(series)
def detect_outliers_iqr(series: pd.Series) -> pd.Series:
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return (series < lower_bound) | (series > upper_bound)

#(b) detect_outliers_zscore(series, threshold=3.0)
def detect_outliers_zscore(series: pd.Series, threshold: float = 3.0) -> pd.Series:
    
    mean = series.mean()
    std = series.std()
    z_scores = ((series - mean) / std).abs()
    return z_scores > threshold

# c)(Stretch) winsorize_series(series, lower=0.05, upper=0.95)
def winsorize_series(series: pd.Series, lower: float = 0.05, upper: float = 0.95) -> pd.Series:
    lower_bound = series.quantile(lower)
    upper_bound = series.quantile(upper)
    return series.clip(lower_bound, upper_bound)
    