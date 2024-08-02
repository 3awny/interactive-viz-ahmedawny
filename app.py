import dash
from dash import dcc, html
from components import navbar  # Custom navbar component
from callbacks import update_charts  # Custom callbacks for updating charts
import dash_bootstrap_components as dbc

# URL for Font Awesome icons CSS
FA621 = "https://use.fontawesome.com/releases/v6.2.1/css/all.css"

# Initialize the Dash app
app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.LUX,  # Bootstrap Lux theme CSS
        FA621,  # Font Awesome Icons CSS
    ],
    use_pages=True  # New in Dash 2.7 - Allows registering pages
)
app.title = "COVID-19 Dashboard"  # Set the title of the app

# Set up the layout of the app
app.layout = dcc.Loading(
    id='loading-page-content',
    children=[html.Div([
        navbar.create_navbar(),  # Include the custom navbar
        dash.page_container  # Container for the registered pages
    ])],
    color='primary',  # Color of the loading spinner
    fullscreen=True  # Display loading spinner fullscreen
)

# Register the callbacks with the app
update_charts.register_callbacks(app)

# Define the server for deployment
server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)  # To run the server in debug mode
