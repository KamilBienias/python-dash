# Etap9. Odcinek: MultiPage App cz.1 i cz.2

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# to tlumi bledy, gdy callbacki nie odnosza sie do app.layout
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    # sekcja wynikowa
    html.Div(id='page-content')
])
# strona glowna
index_page = html.Div([
    html.H3('MENU:'),
    dcc.Link('Wybierz technologię', href='/tech'),
    html.Br(),
    dcc.Link('Podaj swoje doświadczenie', href='/experience')
])
# strona z wyborem technologii
tech_layout = html.Div([
    html.H4('Wybierz technologię z podanych poniżej'),
    dcc.Dropdown(
        id='tech-1-dropdown',
        options=[{'label': i, 'value': i} for i in ['Python', 'SQL', 'Java']],
        # domyslna wartosc
        value='Python'
    ),
    # sekcja wynikowa pozwala podejrzec aktualny wybor
    html.Div(id='tech-1-div'),
    html.Br(),
    dcc.Link('Podaj swoje doświadczenie', href='/experience'),
    html.Br(),
    dcc.Link('Wróc do MENU', href='/')
])

experience_layout = html.Div([
    html.H4('Podaj swoje doświadczenie'),
    dcc.RadioItems(
        id='experience-1-radios',
        options=[{'label': i, 'value': i} for i in ['poniżej 1 roku',
                                                    'od 1 do 3 lat',
                                                    'powyżej 3 lat']],
        value=''
    ),
    # wynik aktualnego wyboru
    html.Div(id='experience-1-div'),
    html.Br(),
    dcc.Link('Wybierz technologię', href='/tech'),
    html.Br(),
    dcc.Link('Wróc do MENU', href='/')
])

@app.callback(
    Output('page-content', 'children'),
    # pathname to parametr komponentu Location
    # on zwraca cala nazwe sciezki po nazwie portu
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/tech':
        return tech_layout
    elif pathname == '/experience':
        return experience_layout
    else:
        return index_page

@app.callback(
    Output('tech-1-div', 'children'),
    [Input('tech-1-dropdown', 'value')]
)
def tech_1_dropdown(value):
    return f'Wybrałeś {value}'

@app.callback(
    Output('experience-1-div', 'children'),
    [Input('experience-1-radios', 'value')]
)
def experience_1_radios(value):
    return f'Wybrałeś {value}'


if __name__ == '__main__':
    app.run_server(debug=True)