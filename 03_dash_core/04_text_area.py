# Etap6. Odcinek: Komponent Pole Tekstkowe - Text Area

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# nazwa __name__ to zmienna srodowiskowa
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    dcc.Textarea(
        placeholder="Wprowadz wartosc",
        style={"width": "100%"},
        value=""  # przyjmuje to co wpisze do pola tekstowego
    ),

    dcc.Textarea(
        placeholder="Wprowadz wartosc",
        style={"width": "60%"}
    ),
])

if __name__ == "__main__":
    app.run_server(debug=True)
