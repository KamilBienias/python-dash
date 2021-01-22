# Etap6. Odcinek: Komponent Tabs (zakladki)

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# nazwa __name__ to zmienna srodowiskowa
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.H3("Hello World - Porownanie"),

    dcc.Tabs(
        children=[
            # pierwsza zakladka
            dcc.Tab(
                label="Python",
                children=[
                    dcc.Markdown(
                        """
                        ```
                        print("Hello World")
                        ```
                        """
                    )
                ]
            ),
            # druga zakladka
            dcc.Tab(
                label="Java",
                children=[
                    dcc.Markdown(
                        """
                        ```
                        System.out.print("Hello world");
                        ```
                        """
                    )
                ]
            )
        ]
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
