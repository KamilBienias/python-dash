# Etap7. Odcinek: Komponent Upload

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# nazwa __name__ to zmienna srodowiskowa
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Upload(html.Button('Upload File')),
    html.Hr(),

    # klasa A wstawia link tak jak <a>
    # to ten niebieski link
    dcc.Upload(html.A('Upload File')),
    html.Hr(),

    dcc.Upload([
        'Drag and drop or ',
        html.A('Select a File')
    ], style={
        'width': '100%',
        'height': '60px',
        'textAlign': 'center',
        'borderWidth': '1px',
        'borderStyle': 'dashed',
        'borderRadius': '5px',  # zaokragla rogi ramki
        'lineHeight': '60px'
    })
])

if __name__ == "__main__":
    app.run_server(debug=True)
