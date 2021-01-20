# Etap5. Odcinek: Pierwsza aplikacja - dostosowanie stylow

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# nazwa __name__ to zmienna srodowiskowa
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    "background": "#b1f2c2",
    "text": "#4c524d"
}

# sekcja glowna
app.layout = html.Div([

    # sekcja
    html.H2("Hello Dash",
            style={
                "color": colors["text"],
                "textAlign": "center"
            }),

    # sekcja
    html.Div("Dash: A web application framework for Python",
             style={
                 "color": colors["text"],
                 "textAlign": "center"
             }),
    # wykres slupkowy
    dcc.Graph(
        figure=go.Figure([
            # pierwszy slad
            go.Bar(
                x=['2017', '2018', '2019'],
                y=[150, 180, 220],
                marker_color='#9ed6f0',  # kolor slupkow
                marker_line_color='#4c524d',  # kolor linii otaczajacej slupki
                marker_line_width=5,  # szerokosc linii otaczajacej slupki
                name="lokalnie"
            ),
            # drugi slupek
            go.Bar(
                x=['2017', '2018', '2019'],
                y=[160, 100, 280],
                marker_color='#077eb5',  # kolor slupkow
                marker_line_color='#4c524d',  # kolor linii otaczajacej slupki
                marker_line_width=5,  # szerokosc linii otaczajacej slupki
                name="online"
            )],
            # layout czyli uklad dla obiektow klasy Figure i Graph
            layout=go.Layout(
                title="Wizualizacja danych",
                plot_bgcolor=colors["background"],  # zielony kolor dla obiektu Figure
                paper_bgcolor="yellow"  # zolty kolor dla obiektu Graph
            )
        )
    )
], style={"backgroundColor": "red"})  # czerwony najbardziej na zewnatrz

if __name__ == "__main__":
    app.run_server(debug=True)
