# Etap6. Odcinek: Komponent Graph

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# nazwa __name__ to zmienna srodowiskowa
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    dcc.Graph(
        figure=go.Figure(
            data=[
                # pierwszy slad
                go.Bar(
                    x=[2017, 2018, 2019],
                    y=[219, 146, 167],
                    name="Sprzedaz USA",  # nazwa z legendy
                    marker=go.bar.Marker(
                        color="rgb(55, 83, 109)"  # ciemny granat
                    )
                ),
                # drugi slad
                go.Bar(
                    x=[2017, 2018, 2019],
                    y=[230, 180, 260],
                    name="Sprzedaz Europa",  # nazwa z legendy
                    marker=go.bar.Marker(
                        color="rgb(26, 118, 255)"  # jasny niebieski
                    )
                )
            ],
            layout=go.Layout(
                title="Sprzedaz",
                showlegend=True
            )
        )
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
