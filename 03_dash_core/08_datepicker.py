# Etap6. Odcinek: Komponent Wybor Daty - Date Picker

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from datetime import datetime as dt

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# nazwa __name__ to zmienna srodowiskowa
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    # domyslnie najpierw pokazuje miesiac a potem dzien
    dcc.DatePickerSingle(
        date=dt(2019, 2, 5)
    ),

    # zmiana formatu daty
    dcc.DatePickerSingle(
        date=dt(2019, 2, 5),
        display_format="YYYY-MM-DD"
    ),

    # kolejna zmiana formatu daty
    dcc.DatePickerSingle(
        date=dt(2019, 2, 5),
        display_format="DD-MM-YYYY"
    ),

    # zakres dat
    dcc.DatePickerRange(
        start_date=dt(2019, 9, 1),
        end_date=dt(2019, 10, 31)
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
