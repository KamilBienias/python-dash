# Etap6. Odcinek: Komponent Markdown

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# nazwa __name__ to zmienna srodowiskowa
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Dla przejrzystosci tutaj argument Markdown.
# Przydaje sie do git
markdown = """
Naglowki:

# H1
## H2
### H3
#### H4
##### H5
###### H6

Znaczniki tekstu:

Na koniec dwie spacje robi nowa linie  
Kursywa: *tekst kursywa* lub _druga kursywa_  
Pogrubienie: **tekst pogrubiony** lub __drugi pogrubiony__  
Kursywa i pogrubienie: **pogrubienie i _kursywa_**  
Przekreslenie: ~~przekreslenie~~

Listy:

Lista uporzadkowana:  
1. Python  
2. SQL  
3. Java 

Lista nieuporzadkowana:  
* Python  
* SQL  
* Java  

Linkowanie:  
[Google](http://www.google.com)  

Kod:  
Uzyj `print("Hello world")`

Blok kodu:
```
import numpy as np

x = np.random.randn(100)
print(x)
```

```
SELECT * FROM products;
```

Table:

|UserID  |Rating  |Age|
|--------|--------|---|
|001     |4.5     |23 |
|002     |5       |34 |

Cytowanie to takie wciecie szare:

> Python jest poreczny i latwy do nauki.

Linie horyzontalne:

---
***
"""

app.layout = html.Div([

    dcc.Markdown(markdown)
])

if __name__ == "__main__":
    app.run_server(debug=True)
