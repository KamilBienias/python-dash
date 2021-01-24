# Etap7. Odcinek: Callback - Multiple Output - Prosty Kalkulator

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# nazwa __name__ to zmienna srodowiskowa
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(
        id='num-1',
        # tylko liczby mozna wprowadzac
        type='number',
        # wartosc domyslna
        value=1
    ),

    dcc.Input(
        id='num-2',
        type='number',
        value=1
    ),
    # pomija naglowki
    html.Table([
        # pierwsza kolumna to nazwa dzialania.
        # Druga kolumna to wartosc jaka dostaniemy od uzytkownika
        html.Tr([html.Td(['x + y']), html.Td(id='tr-1')]),
        html.Tr([html.Td(['x - y']), html.Td(id='tr-2')]),
        html.Tr([html.Td(['x * y']), html.Td(id='tr-3')]),
        html.Tr([html.Td(['x / y']), html.Td(id='tr-4')]),
        html.Tr([html.Td(['x // y']), html.Td(id='tr-5')])
    ])
])

@app.callback(
    #  lista Output bo jest ich 5
    [Output('tr-1', 'children'),
     Output('tr-2', 'children'),
     Output('tr-3', 'children'),
     Output('tr-4', 'children'),
     Output('tr-5', 'children')],
    [Input('num-1', 'value'),
     Input('num-2', 'value')]
)
def update_table(x, y):
    if y == 0:
        return x + y, x - y, x * y, 'Nie dziel przez 0', 'Nie dziel przez 0'
    # wyniki zwraca jako tuple
    return x + y, x - y, x * y, x / y, x // y


if __name__ == "__main__":
    app.run_server(debug=True)
