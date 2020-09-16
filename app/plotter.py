import os
import pandas as pd
import numpy as np

def data4plot(my_data, my_t, year, TW):
    # t
    t = my_t[year]
    # y
    y = my_data[year]
    y = pd.Series(y)
    y = y.fillna(method='backfill')
    # moving average of y
    y = y.rolling(TW).mean()
    # x
    x = np.arange(0,len(y),1)
    
    return t, x, y
