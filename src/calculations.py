import pandas as pd
import numpy as np

from scipy.stats import norm

def value_at_risk(data, confidence_level):
    return data.quantile(confidence_level, axis=0, interpolation="higher")

def expected_shortfall(data, confidence_level):
    return data[data.lt(value_at_risk(data, confidence_level), axis=1)].mean()

def sharpe_ratio(data):
    data_log = np.log(data).pct_change()
    data_log = data_log.fillna(0)
    days = (data.index.max() - data.index.min()).days
    print(days)
    return days**(0.5)*data_log.mean() / data_log.std()
    