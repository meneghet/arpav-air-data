from app import app
from flask import render_template

import numpy as np

from bokeh.embed import components
from bokeh.resources import INLINE
from bokeh.plotting import figure, output_file, show

from app.get_data import get_data
from app.plotter import data4plot


#
provincia = 'padova'
location = 'PD - Arcella'
year_range = np.arange(2013,2020+1)
quality_idx = 'NO2'
TW = 30

my_data, my_t = get_data(provincia, location, year_range, quality_idx)

year = 2019
t, x, y = data4plot(my_data, my_t, year, TW)

# init a basic bar chart:
# http://bokeh.pydata.org/en/latest/docs/user_guide/plotting.html#bars
fig = figure(plot_width=600, plot_height=600)
fig.line(
    x=x,
    y=y,
    # x=[1, 2, 3, 4],
    # y=[1.7, 2.2, 4.6, 3.9],
    color='navy'
)

show(fig)