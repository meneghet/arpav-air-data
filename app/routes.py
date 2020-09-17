from app import app
from flask import render_template

from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE

import numpy as np

from app.get_data import get_data
from app.plotter import data4plot, data2df

from bokeh.models import CustomJS, Select, ColumnDataSource
from bokeh.models.widgets import RadioButtonGroup
from bokeh.layouts import column, row



@app.route('/')
@app.route('/index')
def index():

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
    select = Select(title="monthly csv-s",  options=LABELS)
    
    source = ColumnDataSource(df_year[2017])
    p = figure(plot_width=600, plot_height=300, title=F'{quality_idx} in {provincia} ({location})')
    r = p.line(x='time', y='y', color='navy',
             source = source)
             
    def update_plot(attrname, old, new):
        source.data =  df_year[int(select.value)]
        
    select.on_change('value', update_plot)

    # grab the static resources
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    # render template
    script, div = components(column(select, p))
    html = render_template(
        'index.html',
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources,
    )
    return html
    






