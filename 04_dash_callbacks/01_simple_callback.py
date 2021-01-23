# Etap7. Odcinek: Prosty Callback

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# nazwa __name__ to zmienna srodowiskowa
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    dcc.Input(id="input-1",
              value="",  # nie ma domyslnej wartosci
              type="text"),

    # tu wyswietla wszystko co wpisuje
    html.Div(id="div-1",
             children="")

])


# interaktywnosc
@app.callback(
    # z dash.dependencies
    Output(component_id="div-1",
           component_property="children"  # to chcemy zmienic
           ),
    # z dash.dependencies
    [Input(component_id="input-1",
           component_property="value"  # taka wartosc chce uzyskac z tego komponentu
           )]
)
def update_div(input):
    return f"Wprowadzono: {input}"

# tu jest def callback()
# https://github.com/plotly/dash/blob/dev/dash/dash.py


if __name__ == "__main__":
    app.run_server(debug=True)
