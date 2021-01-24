# Etap7. Odcinek: Callback - Graph

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df = pd.read_csv("https://ml-repository-krakers.s3-eu-west-1.amazonaws.com/dash_course/data.csv")
print(df)

# nazwa __name__ to zmienna srodowiskowa
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Graph(id="graph-1"),
    dcc.Slider(
        id="slider-1",
        min=df["year"].min(),
        max=df["year"].max(),
        # domyslna wartosc ustawiona na rok poczatkowy
        value=df["year"].min(),
        # podpisy
        marks={str(year): str(year) for year in df["year"].unique()},
        step=None
    )
])


@app.callback(
    Output("graph-1", "figure"),
    # ze slidera chce wyciagnac to co jest w parametrze value
    [Input("slider-1", "value")]
)
def update_graph(selected_year):
    # dff to dataframe filter
    dff = df.query(f"year == {selected_year}")
    # lista sladow dla kazdego kontynentu
    traces = []
    for cont in df["continent"].unique():
        dff_cont = dff[dff["continent"] == cont]
        traces.append(
            go.Scatter(
                # x to PKB na osobe
                x=dff_cont["gdpPercap"],
                # y to oczekiwana dlugosc zycia
                y=dff_cont["lifeExp"],
                mode="markers",
                # nazwa sladu to kontynent
                name=cont,
                # przezroczystosc punktow
                opacity=0.6,
                marker={
                    # rozmiar punktow
                    "size": 15,
                    # linia dla kazdego punktu
                    "line": {"width": 1.5, "color": "white"}
                },
                # sam znalazlem jak wyswietlic nazwe kraju po najechaniu myszka
                hoverinfo="text",
                hovertext=dff_cont["country"],
                # hoveron="points"  # to nie mialo wplywu

            )
        )


    # zwraca slownik
    return {
        "data": traces,
        "layout": go.Layout(
            title_text="Wykres",
            xaxis={
                "type": "log",
                "title": "PKB per capita"
            },
            yaxis={
                "title": "Oczekiwana dlugosc zycia"
            },
            # wyswietlenie najblizszego punktu po najechaniu myszka
            hovermode="closest"
        )
    }

if __name__ == "__main__":
    app.run_server(debug=True)
