# Etap6. Odcinek: Komponent Lista Wyboru - Checklist

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# nazwa __name__ to zmienna srodowiskowa
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    dcc.Checklist(
        options=[
            {"label": "Python", "value": "py"},
            {"label": "SQL", "value": "sql"},
            {"label": "Java", "value": "jar"}
        ]
    ),

    html.Br(),

    dcc.Checklist(
        options=[
            {"label": "Python", "value": "py"},
            {"label": "SQL", "value": "sql"},
            {"label": "Java", "value": "jar"}
        ],
        # domyslna zaznaczona wartosc
        value=["py"]
    ),

    html.Br(),

    dcc.Checklist(
        options=[
            {"label": "Python", "value": "py"},
            {"label": "SQL", "value": "sql"},
            {"label": "Java", "value": "jar"}
        ],
        # domyslne zaznaczone wartosci
        value=["py", "sql"]
    ),

    html.Br(),

    # trzecia opcja nieaktywna
    dcc.Checklist(
        options=[
            {"label": "Python", "value": "py"},
            {"label": "SQL", "value": "sql"},
            {"label": "Java", "value": "jar", "disabled": True}
        ],
        # domyslne zaznaczone wartosci
        value=["py", "sql"]
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
