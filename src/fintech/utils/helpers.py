"""
Utility functions for the fintech package.
"""
from typing import Union, List
import pandas as pd
import numpy as np

def validate_date_format(date_str: str) -> bool:
    """
    Validate if a string is in the correct date format (YYYY-MM-DD).
    """
    try:
        pd.to_datetime(date_str)
        return True
    except ValueError:
        return False

def calculate_returns(
    prices: Union[List[float], pd.Series], 
    log_returns: bool = False
) -> Union[List[float], pd.Series]:
    """
    Calculate returns from a series of prices.
    """
    if log_returns:
        return np.log(prices / prices.shift(1))
    return prices.pct_change() 