# Etap6. Odcinek: Komponent HTML DIV

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# nazwa __name__ to zmienna srodowiskowa
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.Div(
        "Przykladowa sekcja",
        style={
            "color": "darkblue",  # kolor czcionki
            "fontSize": 18,
            "background-color": "lightblue",
            "text-align": "center",
            "border": "4px solid Grey",
            "border-style": "dashed"  # linia przerywana
        }
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
