import os
import pandas as pd
import numpy as np

def get_data(provincia, location, year_range, quality_idx):
    
    # load last saved dataset (just one)
    save_dir = os.path.join('datasets',provincia)
    fnames = os.listdir(save_dir)
    df = pd.read_csv(os.path.join(save_dir, F'{location}.csv'), index_col=0)
    
    # custom year range
    df.index = pd.to_datetime(df.index)
    all_idx = [x for x in df.index.values]
    year_idx = pd.to_datetime(all_idx).year.values
    year_range = np.unique(year_idx)
    
    my_data = {}
    my_t = {}
    for year in year_range:
        # data from this year
        df_ = df.loc[year_idx == year, quality_idx]
        # convert to numeric
        df_ = pd.to_numeric(df_, errors='coerce')
        # store in dataframe
        my_data[year] = df_.values
        my_t[year] = df_.index
    
    return my_data, my_t