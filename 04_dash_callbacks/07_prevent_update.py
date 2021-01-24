# Etap7. Odcinek: Callback - Prevent Update

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    # jesli nie ustawie n_clicks to jest None.
    html.Button('Click Here', id='button-1'),
    # tekst wynikowy
    html.Div(id='div-1')
])

@app.callback(
    Output('div-1', 'children'),
    [Input('button-1', 'n_clicks')]
)
def update_output(n_clicks):
    # wypisuje do konsoli ilosc klikniec
    print(n_clicks)
    # jesli n_clicks jest None to zapobiega zaktualizowaniu outputu
    if n_clicks is None:
        raise PreventUpdate
    else:
        # jesli chociaz raz kliknelismy w przycisk
        return f'Bardzo cenna informacja! Kliknąłeś {n_clicks} razy!'

if __name__ == "__main__":
    app.run_server(debug=True)
