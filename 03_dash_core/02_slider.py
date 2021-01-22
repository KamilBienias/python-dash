# Etap6. Odcinek: Komponent Slider

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# nazwa __name__ to zmienna srodowiskowa
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.Label("Slider"),

    # bez podpisow
    dcc.Slider(
        min=0,
        max=3,
        step=1
    ),

    html.Br(),

    # z podpisami
    dcc.Slider(
        min=0,
        max=3,
        step=1,
        marks={0: "Label 0", 1: "Label 1", 2: "Label 2", 3: "Label 3"}
    ),

    html.Br(),

    # z dict comprehentions
    dcc.Slider(
        min=0,
        max=3,
        step=1,
        marks={i: f"Label {i}" for i in range(4)}
    ),

    html.Br(),

    # niektore podpisy moga byc puste
    dcc.Slider(
        min=0,
        max=3,
        step=1,
        marks={1: "Label 1", 2: "Label 2"}
    ),
])

if __name__ == "__main__":
    app.run_server(debug=True)
