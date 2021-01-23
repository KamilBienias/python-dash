# Etap7. Odcinek: Callback - Button

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# nazwa __name__ to zmienna srodowiskowa
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    # sekcja z danymi wejsciowymi
    html.Div([
        # okienko do wpisywania. Parametr value to zawartosc tego co wpisano
        dcc.Input(id="input-1", type="text", value="example", placeholder="Wprowadz tekst...")
    ]),

    # n_clicks ma domyslnie None
    html.Button(id="button-1", children="Submit", n_clicks=0),

    # sekcja z danymi wyjsciowymi
    html.Div(id="div-1", children="Wprowadz tekst i przycisnij Submit")
])


@app.callback(
    Output(component_id="div-1", component_property="children"),
    [Input(component_id="input-1", component_property="value"),
     Input(component_id="button-1", component_property="n_clicks")]
)
def update_output(value, n_clicks):
    return f"Wprowadziles {value} i nacisnales przycisk {n_clicks} razy."


if __name__ == "__main__":
    app.run_server(debug=True)
