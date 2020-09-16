from app import app
from flask import render_template

import numpy as np

from bokeh.embed import components
from bokeh.resources import INLINE
from bokeh.plotting import figure, output_file#, show
from bokeh.io import show
from app.get_data import get_data
from app.plotter import data4plot
from bokeh.layouts import column, row, widgetbox

# from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Slider, TextInput

import pandas as pd


from bokeh.models import CustomJS, Select



#
provincia = 'padova'
location = 'PD - Arcella'
year_range = np.arange(2013,2020+1)
quality_idx = 'NO2'
TW = 30

my_data, my_t = get_data(provincia, location, year_range, quality_idx)

year = 2019
t, x, y = data4plot(my_data, my_t, year, TW)

t = pd.to_datetime(t)
# print(t)


# Set up widgets
text = TextInput(title="title", value='')
offset = Slider(title="offset", value=0.0, start=-5.0, end=5.0, step=0.1)
amplitude = Slider(title="amplitude", value=1.0, start=-5.0, end=5.0)
phase = Slider(title="phase", value=0.0, start=0.0, end=2*np.pi)
freq = Slider(title="frequency", value=1.0, start=0.1, end=5.1)


fig = figure(plot_width=600, plot_height=600, title='abc')
fig.line(
    x=t,
    y=y,
    color='navy'
    )

# Set up callbacks
def update_title(attrname, old, new):
    fig.title.text = text.value

text.on_change('value', update_title)
    
# Set up layouts and add to document
inputs = widgetbox(text, offset, amplitude, phase, freq)

show(row(inputs, fig))
