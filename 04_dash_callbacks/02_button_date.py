# Etap7. Odcinek: Callback - 3 x Button + Timestamp

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from datetime import datetime

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# nazwa __name__ to zmienna srodowiskowa
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    # n_clicks_timestamp=0 zwraca liczbe milisekund od 1970-01-01
    html.Button(id="btn-1", children="Button1", n_clicks_timestamp=0),
    html.Button(id="btn-2", children="Button2", n_clicks_timestamp=0),
    html.Button(id="btn-3", children="Button3", n_clicks_timestamp=0),
    # sekcja z wynikami, children nie trzeba pisac
    html.Div(id="div-1")
])

@app.callback(
    # w komponencie o id="div-1" chcemy ustawic parametr component_property="children"
    Output("div-1", "children"),
    [Input("btn-1", "n_clicks_timestamp"),
     Input("btn-2", "n_clicks_timestamp"),
     Input("btn-3", "n_clicks_timestamp")]
)
def displayClick(btn1, btn2, btn3):
    # jesli czas przycisku pierwszego jest wiekszy od drugiego i trzeciego
    if int(btn1) > int(btn2) and int(btn1) > int(btn3):
        msg = "Button1 zostal wcisniety jako ostatni."
    elif int(btn2) > int(btn1) and int(btn2) > int(btn3):
        msg = "Button2 zostal wcisniety jako ostatni."
    elif int(btn3) > int(btn1) and int(btn3) > int(btn2):
        msg = "Button3 zostal wcisniety jako ostatni."
    else:
        msg = "Zaden przycisk nie zostal wcisniety"
    # bedzie sekcja w sekcji. Callback zwraca to do parametru children
    # komponentu o id="div-1"
    return html.Div([
        # funkcja fromtimestamp czyta czas w postaci sekund
        html.Div(f"btn1: {datetime.fromtimestamp(btn1 / 1000)}"),
        html.Div(f"btn2: {datetime.fromtimestamp(btn2 / 1000)}"),
        html.Div(f"btn3: {datetime.fromtimestamp(btn3 / 1000)}"),
        html.Div(msg)
    ])


if __name__ == "__main__":
    app.run_server(debug=True)
