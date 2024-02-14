import pandas as pd
from dash import Dash, dcc, html
from plotly.express import line

# Load the data from CSV file
DATA_PATH = "./formatted_data.csv"
data = pd.read_csv(DATA_PATH)
data = data.sort_values(by='date')

# Initialize the Dash app
app = Dash(__name__)

# ------------- Create HTML and Dash components --------------

# Create header
header = html.H1(
            'Pink Morsel Sales Visualizer',
            id='header'
            )

# Create visualization
line_chart = line(data, x='date', y='sales', title='Pink Morsel Sales')
line_chart.update_layout(
    xaxis_title='Date',
    yaxis_title='Sales'
)
visualization = dcc.Graph(
    id='visaulizaion',
    figure=line_chart
)

# ------------------ Define app layout -----------------------
app.layout = html.Div(
    [
        header,
        visualization
    ]
)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)