import dash
from dash import dcc, html
from components import navbar
from callbacks import update_charts
import dash_bootstrap_components as dbc

FA621 = "https://use.fontawesome.com/releases/v6.2.1/css/all.css"


# Initialize the app
app = dash.Dash(__name__,     external_stylesheets=[
        dbc.themes.LUX,  # Dash Themes CSS
        FA621,  # Font Awesome Icons CSS
    ], use_pages=True)  # New in Dash 2.7 - Allows us to register pages
app.title = "COVID-19 Dashboard"

# Set up the layout
app.layout = dcc.Loading(id='loading-page-content', children=[html.Div([    
        # dcc.Location(id='url', refresh=False),
        navbar.create_navbar(),
        dash.page_container
    ])]
    ,color='primary', fullscreen=True)

# Register callbacks
update_charts.register_callbacks(app)

server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)
