# Etap6. Odcinek: Komponent Dropdown

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# nazwa __name__ to zmienna srodowiskowa
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.Label("Wybierz preferowana technologie:"),

    # domyslnie ma opcje wyszukiwania
    dcc.Dropdown(
        # label to wyswietlone, a value zapamietane przez dash
        options=[
            {"label": "Python", "value": "py"},
            {"label": "SQL", "value": "sql"},
            {"label": "Java", "value": "jar"}
        ]
    ),

    dcc.Dropdown(
        # label to wyswietlone, a value zapamietane przez dash
        options=[
            {"label": "Python", "value": "py"},
            {"label": "SQL", "value": "sql"},
            {"label": "Java", "value": "jar"}
        ],
        # domyslna wartosc jaka przyjmie dropdown
        value="py"
    ),

    dcc.Dropdown(
        # label to wyswietlone, a value zapamietane przez dash
        options=[
            {"label": "Python", "value": "py"},
            {"label": "SQL", "value": "sql"},
            {"label": "Java", "value": "jar"}
        ],
        # domyslna wartosc jaka przyjmie dropdown
        value="py",
        # mozna wybrac wiecej niz jedna opcje
        multi=True
    ),

    dcc.Dropdown(
        # label to wyswietlone, a value zapamietane przez dash
        options=[
            {"label": "Python", "value": "py"},
            {"label": "SQL", "value": "sql"},
            {"label": "Java", "value": "jar"}
        ],
        # wylaczenie opcji przeszukiwania
        searchable=False
    ),

    dcc.Dropdown(
        # label to wyswietlone, a value zapamietane przez dash
        options=[
            {"label": "Python", "value": "py"},
            {"label": "SQL", "value": "sql"},
            {"label": "Java", "value": "jar"}
        ],
        # wylaczenie opcji przeszukiwania
        placeholder="Wybierz technologie..."
    ),

    dcc.Dropdown(
        # label to wyswietlone, a value zapamietane przez dash
        options=[
            {"label": "Python", "value": "py"},
            {"label": "SQL", "value": "sql"},
            {"label": "Java", "value": "jar"}
        ],
        # wylaczenie dropdownu
        disabled=True
    ),

])

if __name__ == "__main__":
    app.run_server(debug=True)
