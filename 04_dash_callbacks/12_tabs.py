# Etap7. Odcinek: Budowa interaktywnych zakladek - Tabs

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    # zakladki
    dcc.Tabs(
        id='tabs-1',
        children=[
            # Tab to jedna zakladka
            dcc.Tab(label='Python', value='py'),
            # druga zakladka
            dcc.Tab(label='SQL', value='sql')
        ],
        # domyslna wartosc
        value='py'
    ),
    # sekcja wynikowa
    html.Div(id='div-1')
])

@app.callback(
    Output('div-1', 'children'),
    [Input('tabs-1', 'value')]
)
def render_content(tab):
    if tab == 'py':
        return html.Div([
            dcc.Markdown("""
            ```
            print('Hello World')
            ```
            """)
        ])
    elif tab == 'sql':
        return html.Div([
            # sql po to zeby mogl kolory zrobic
            dcc.Markdown("""
            ```sql  
            SELECT * FROM products;
            ```
            """)
        ])


if __name__ == '__main__':
    app.run_server(debug=True)