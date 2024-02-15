# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
# (Press CTRL+C to quit)

import pandas as pd
from dash import Dash, dcc, html, Input, Output # dcc - Dash Core Components
from plotly.express import line

# the path to the output CSV file
DATA_PATH = "./output.csv"
COLORS = {
    'primary': '#FFC1D5 ', # main bg, graph bg 
    'secondary': '#FF86AE', # graph itself, header
    'font': '#B24C6D' # hader text font color
}

# load in data
data = pd.read_csv(DATA_PATH)
data = data.sort_values(by='date')

# Initialize the Dash app
app = Dash(__name__)

# ------------- Create HTML and Dash components --------------

# Component-1: Create header
header = html.H1(
    'Pink Morsel Sales Visualizer',
    id='header',
    style={
        'background-color': COLORS['secondary'],
        'color': COLORS['font'],
        'border-radius': '20px'
    }
)

# Component-2 :Create visualization
def generate_figure(chart_data):
    line_chart = line(data, x='date', y='sales', title='Pink Morsel Sales')
    line_chart.update_layout(
        xaxis_title='Date',
        yaxis_title='Sales',
        plot_bgcolor=COLORS['secondary'],
        paper_bgcolor=COLORS['primary'],
        font_color=COLORS['font']
    )
    return line_chart

visualization = dcc.Graph(
    id='visaulizaion',
    figure=generate_figure(data)
)

# Component-3: Create region picker
region_picker = dcc.RadioItems(
    ['all', 'east', 'south', 'west', 'north'],
    'all',
    id='region-picker',
    inline=True,
    style={
        'padding': '20px'
    }
)
region_picker_wrapper = html.Div(
    [
        region_picker
    ],
    style={
        'font-size': '200%',
        'background-color': COLORS['secondary'],
        'color': COLORS['font'],
        'border-radius': '20px'
    }
)

@app.callback(
    Output(visualization, 'figure'),
    Input(region_picker, 'value')
)
def upgrade_graph(region):
    # filter data based on region
    if region == 'all':
        trimmed_data = data
    else:
        trimmed_data = data[data['region'] == region]

    # generate a new line chart with filtered data
    figure = generate_figure(trimmed_data)
    return figure

# ------------------ Define app layout -----------------------
app.layout = html.Div(
    [
        header,
        visualization,
        region_picker_wrapper,
        html.Br()
    ],
    style={
        'textAlign': 'center',
        'background-color': COLORS['primary'],
        'border-radius': '20px',
        'margin': '20px'
    }
)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
    # debug=True stands for "hot-reloading"
    # This means that Dash will automatically refresh your browser when you make a change in your code.