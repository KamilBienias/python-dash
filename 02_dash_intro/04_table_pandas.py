# Etap5. Odcinek: Pierwsza aplikacja - tabela + pandas

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# nazwa __name__ to zmienna srodowiskowa
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


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
# zeby nie byla za duza tabela
df = df[:30]
# jesli spolka miala mniej niz 30 notowan to bierze dlugosc obiektu df
min_val = min(len(df), 30)

app.layout = html.Div([

    html.H4("Notowania spolki Amazon"),

    html.Table([

        # list comprehensions tworzace Th
        html.Tr([html.Th(col) for col in df.columns])] +
        # wiersze tabeli. Wycina i-ty wiersz oraz kolumne col
        [html.Tr([html.Td(df.iloc[i][col]) for col in df.columns]) for i in range(min_val)]
    )


])

if __name__ == "__main__":
    app.run_server(debug=True)
