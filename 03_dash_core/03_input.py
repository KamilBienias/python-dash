# Etap6. Odcinek: Komponent Input

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# nazwa __name__ to zmienna srodowiskowa
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    dcc.Input(
        type="text"
    ),

    # bez tego jest obok kolejny input
    html.Br(),

    dcc.Input(
        type="text",
        placeholder="Wprowadz tekst..."
    ),

    dcc.Input(
        type="number",
        placeholder="Wprowadz liczbe..."
    ),

    dcc.Input(
        type="password",
        placeholder="Wprowadz haslo..."
    ),

    html.Br(),

    dcc.Input(
        type="email",
        placeholder="Wprowadz email..."
    ),


])

if __name__ == "__main__":
    app.run_server(debug=True)
