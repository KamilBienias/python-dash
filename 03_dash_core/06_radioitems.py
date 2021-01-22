# Etap6. Odcinek: Komponent RadioItems

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# nazwa __name__ to zmienna srodowiskowa
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    dcc.RadioItems(
        options=[
            {"label": "Python", "value": "py"},
            {"label": "SQL", "value": "sql"},
            {"label": "Java", "value": "jar"}
        ]
    ),

    html.Br(),

    # wartosc domyslna
    dcc.RadioItems(
        options=[
            {"label": "Python", "value": "py"},
            {"label": "SQL", "value": "sql"},
            {"label": "Java", "value": "jar"}
        ],
        value="py"
    ),

    html.Br(),

    # wartosc domyslna i wylacza trzecia opcje
    dcc.RadioItems(
        options=[
            {"label": "Python", "value": "py"},
            {"label": "SQL", "value": "sql"},
            {"label": "Java", "value": "jar", "disabled": True}
        ],
        value="py"
    ),

    html.Br(),

    # wartosc domyslna i zmiana wygladu ukladu na poziomy
    dcc.RadioItems(
        options=[
            {"label": "Python", "value": "py"},
            {"label": "SQL", "value": "sql"},
            {"label": "Java", "value": "jar"}
        ],
        value="py",
        labelStyle={"display": "inline-block"}
    ),
])

if __name__ == "__main__":
    app.run_server(debug=True)
