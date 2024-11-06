import pytest
import pandas as pd
import numpy as np
from fintech.analysis.indicators import calculate_moving_average, calculate_rsi

def test_calculate_moving_average():
    data = pd.Series([1, 2, 3, 4, 5])
    ma = calculate_moving_average(data, window=3)
    assert len(ma) == len(data)
    assert pd.isna(ma[0])  # First two values should be NaN
    assert ma[2] == 2.0    # First valid MA value

def test_calculate_rsi():
    data = pd.Series([10, 12, 11, 13, 15, 14, 16])
    rsi = calculate_rsi(data, period=3)
    assert len(rsi) == len(data)
    assert all(0 <= x <= 100 for x in rsi.dropna())
