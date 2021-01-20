# Etap3. Odcinek: Pierwsza aplikacja

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

# nazwa __name__ to zmienna srodowiskowa
app = dash.Dash(__name__)

# wyglad aplicji
app.layout = html.Div(children=[

    html.H2(children="Hello Dash!"),

    dcc.Graph(
        figure=go.Figure([
            # pierwszy slad
            go.Bar(
                x=['2017', '2018', '2019'],
                y=[150, 180, 220],
                name='lokalnie'
            ),
            # drugi slad
            go.Bar(
                x=['2017', '2018', '2019'],
                y=[80, 160, 240],
                name='online'
            )
        ])
    )
])

if __name__ == "__main__":
    app.run_server()