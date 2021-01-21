# Etap5. Odcinek: Pierwsza aplikacja - wykres ceny akcji i wolumenu obrotu

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go


# ticker AMZN jest ze strony stooq. Mozna inne stamtad brac
def fetch_financial_data(company='AMZN'):
    """
    This function fetch stock market quotations.
    """
    import pandas_datareader.data as web
    return web.DataReader(name=company, data_source='stooq')


df = fetch_financial_data()
# resetuje indeks zeby miec date jako kolumne
df.reset_index(inplace=True)
# daty pozniejsze niz podana
df[df.Date > '2019-01-01']

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# nazwa __name__ to zmienna srodowiskowa
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.H4("Notowania spolki Amazon"),

    dcc.Graph(
        figure=go.Figure(
            data=[
                go.Scatter(
                    x=df.Date,
                    y=df.Close,
                    mode="lines",
                    fill="tozeroy",
                    name="Amazon"  #
                )
            ],
            layout=go.Layout(
                yaxis_type="log",  # typ osi y logarytmiczny
                height=500,
                title_text="Wykres ceny",
                showlegend=True
            )
        )
    ),
    dcc.Graph(
        figure=go.Figure(
            data=[
                go.Bar(
                    x=df.Date,
                    y=df.Volume,
                    name="Wolumen"
                )
            ],
            layout=go.Layout(
                yaxis_type="log",
                height=300,
                title_text="Wykres wolumenu",
                showlegend=True
            )
        )
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
