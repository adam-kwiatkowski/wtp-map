import pandas as pd
import plotly.express as px
import requests
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from dotenv import dotenv_values, find_dotenv

config = dotenv_values(find_dotenv())
if 'API_KEY' not in config:
    raise Exception('API_KEY not found in .env file')
if 'MAPBOX_TOKEN' not in config:
    raise Exception('MAPBOX_TOKEN not found in .env file')

mapbox_token = config['MAPBOX_TOKEN']
api_key = config['API_KEY']
api_url = 'https://api.um.warszawa.pl/api/action/busestrams_get/'
api_params = {
    'resource_id': 'f2e5503e927d-4ad3-9500-4ab9e55deb59',
    'apikey': api_key,
    'type': 1,
    'line': 512,
}

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = Dash(__name__, external_stylesheets=external_stylesheets)

px.set_mapbox_access_token(mapbox_token)

app.layout = html.Div([
    dcc.Graph(id='map', animate=True),
    dcc.Interval(
        id='interval-component',
        interval=3000,
        n_intervals=0
    )
])


@app.callback(Output('map', 'figure'), [Input('interval-component', 'n_intervals')])
def update_map(n):
    response = requests.get(api_url, params=api_params)
    data = response.json()

    df = pd.DataFrame(data['result'])

    fig = px.scatter_mapbox(
        df,
        lat='Lat',
        lon='Lon',
        color='Lines',
    )

    fig.update_layout()

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
