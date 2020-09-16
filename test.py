from app import app
from flask import render_template

import numpy as np
import pandas as pd

from bokeh.embed import components
from bokeh.resources import INLINE
from bokeh.plotting import figure, output_file#, show
from bokeh.io import show
from app.get_data import get_data
from app.plotter import data4plot, data2df
from bokeh.layouts import column, row, widgetbox

from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import RadioButtonGroup

from bokeh.models import CustomJS, Select

#
provincia = 'padova'
location = 'PD - Arcella'
year_range = np.arange(2013,2020+1)
quality_idx = 'NO2'
TW = 30

my_data, my_t = get_data(provincia, location, year_range, quality_idx)
df_year = {}
for year in [2017, 2018, 2019]:
    df_year[year] = data2df(my_data, my_t, year, TW)

LABELS = ["2017", "2018", "2019"]
radio_button_group = RadioButtonGroup(labels=LABELS, active=0)
select = Select(title="Year",  options=LABELS)

source = ColumnDataSource(df_year[2017])
p = figure(plot_width=600, plot_height=300, title=F'{quality_idx} in {provincia} ({location})')
r = p.line(x='time', y='y', color='navy',
         source = source)
         
def update_plot(attrname, old, new):
    source.data =  df_year[int(select.value)]
    
select.on_change('value', update_plot)

layout = column(row(select, width=400), p)

curdoc().add_root(layout)


