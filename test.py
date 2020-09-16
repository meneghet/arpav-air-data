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

from bokeh.io import curdoc

# from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import RadioButtonGroup

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
d2019 = {'time': t, 'y': y}
df2019 = pd.DataFrame(data=d2019)

year = 2018
t, x, y = data4plot(my_data, my_t, year, TW)
d2018 = {'time': t, 'y': y}
df2018 = pd.DataFrame(data=d2018)

year = 2017
t, x, y = data4plot(my_data, my_t, year, TW)
d2017 = {'time': t, 'y': y}
df2017 = pd.DataFrame(data=d2017)



LABELS = ["2017", "2018", "2019"]
radio_button_group = RadioButtonGroup(labels=LABELS, active=0)
select = Select(title="monthly csv-s",  options=LABELS)

source = ColumnDataSource(df2017)
p = figure(plot_width=600, plot_height=300, title='abc')
r = p.line(x='time', y='y', color='navy',
         source = source)
         
def update_plot(attrname, old, new):
    
    if select.value == '2017':
        newSource = df2017
    if select.value == '2018':
        newSource = df2018
    if select.value == '2019':
        newSource = df2019
    source.data =  newSource
    
select.on_change('value', update_plot)

layout = column(row(select, width=400), p)


# Set up layouts and add to document
# show(layout)
curdoc().add_root(layout)


