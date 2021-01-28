# Etap8. Odcinek: Eksport danych z tabeli

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import dash_table

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H4("Pobiera tabele do pliku excela"),
    # ta tabele pobiera jako excel
    dash_table.DataTable(
        columns=[
            {'name': 'Year', 'id': 'year'},
            {'name': 'Poland', 'id': 'poland'},
            {'name': 'Import', 'id': 'import'},
            {'name': 'Export', 'id': 'export'}
        ],
        data=[
            # pierwszy slownik to pierwszy wiersz
            {'year': 2018,
             'poland': 100,
             'import': 65,
             'export': 35},
            # drugi slownik to drugi wiersz
            {'year': 2019,
             'poland': 100,
             'import': 66,
             'export': 34}
        ],
        # eksportuje do pliku excel
        export_format='xlsx',
        # naglowki tez sie eksportuja
        export_headers='display'
    ),
    html.H4("Pobiera tabele do pliku csv"),
    # ta tabele pobiera jako csv
    dash_table.DataTable(
        columns=[
            {'name': 'Year', 'id': 'year'},
            {'name': 'Poland', 'id': 'poland'},
            {'name': 'Import', 'id': 'import'},
            {'name': 'Export', 'id': 'export'}
        ],
        data=[
            {'year': 2018,
             'poland': 100,
             'import': 65,
             'export': 35},
            {'year': 2019,
             'poland': 100,
             'import': 66,
             'export': 34}
        ],
        # eksportuje do pliku excel
        export_format='csv'
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)