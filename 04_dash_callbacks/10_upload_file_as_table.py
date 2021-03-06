# Etap7. Odcinek: Aplikacja - Zaladowanie dowolnego pliku (csv, xls) jako Tabeli

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output, State
import base64  # przekodowuje dane binarne do ASCII i odwrotnie
import io  # input-output ktora odczytuje string jako plik
import pandas as pd
from datetime import datetime
import dash_table

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Upload(
        id='upload-1',
        children=html.Div([
            'Drag and drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'textAlign': 'center',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'lineHeight': '60px'
        },
        multiple=True  # aby mozna bylo wiecej plikow zaladowac
    ),
    # to nasz output
    html.Div(id='div-1')
])

# date jest w postaci timestamp
def parse_contents(content, name, date):
    # content_type zawiera dane przed przecinkiem a content_string po przecinku
    content_type, content_string = content.split(',')
    # tekst
    decoded = base64.b64decode(content_string)
    try:
        # jesli w nazwie pliku jest csv
        if 'csv' in name:
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in name:
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'Wystąpił błąd podczas przetwarzania pliku.'
        ])


    return html.Div([
        html.H5(name),
        # zamienia date z timestamp do wygodnego odczytu
        html.H6(datetime.fromtimestamp(date)),

        # tabele wyswietla w sekcji o id='div-1'
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name': col, 'id': col} for col in df.columns]
        ),
        html.Hr(),
        # na dole surowa zawartosc, pierwsze 300 znakow
        html.Div('Raw Content'),
        html.Pre(content[:300] + '...')
    ])




@app.callback(
    Output('div-1', 'children'),
    [Input('upload-1', 'contents')],
    # State pozwala modyfikowac tylko jesli pliki sa zaladowane
    [State('upload-1', 'filename'),  # lista plikow
     State('upload-1', 'last_modified')]  # lista dat
)
def update_output(list_of_contents, list_of_names, list_of_dates):
    print(list_of_contents)
    print(list_of_names)
    print(list_of_dates)
    # jesli cokolwiek zaladowalismy
    if list_of_contents is not None:
        children = [
            parse_contents(content, name, date) for content, name, date in zip(list_of_contents,
                                                                               list_of_names,
                                                                               list_of_dates)
        ]
        return children


if __name__ == "__main__":
    app.run_server(debug=True)
