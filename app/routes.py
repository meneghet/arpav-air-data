from app import app
from flask import render_template

from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE

import numpy as np

from app.get_data import get_data
from app.plotter import data4plot

from bokeh.models import CustomJS, Select
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

    year = 2019
    t, x, y = data4plot(my_data, my_t, year, TW)
    
    p = figure(plot_width=600, plot_height=600, title='abc')
    p.line(
        x=x,
        y=y,
        color='navy'
    )
    
    LABELS = ["2017", "2018", "2019"]
    select = Select(title="monthly csv-s",  options=LABELS)
    layout = column(row(select, width=400), p)
    
    select = Select(title="Option:", value="foo", options=["foo", "bar", "baz", "quux"])
    select.js_link('value', p, 'title')

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
