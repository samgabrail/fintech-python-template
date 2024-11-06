"""
Technical analysis indicators and financial metrics.
"""
import pandas as pd
import numpy as np

def calculate_moving_average(data: pd.Series, window: int) -> pd.Series:
    """
    Calculate the simple moving average for a given series.
    """
    return data.rolling(window=window).mean()

def calculate_rsi(data: pd.Series, period: int = 14) -> pd.Series:
    """
    Calculate the Relative Strength Index (RSI).
    """
    delta = data.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    
    rs = gain / loss
    return 100 - (100 / (1 + rs))
