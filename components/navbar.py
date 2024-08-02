import dash_bootstrap_components as dbc
from dash import html
import dash_bootstrap_components as dbc

# Function to create the app navbar
def create_navbar():
    # Define the structure of the navbar using dbc.Navbar
    navbar = dbc.Navbar(
        dbc.Container(
            [
                # Define a row within the container
                dbc.Row(
                    [
                        # First column with the brand name of the dashboard
                        dbc.Col(
                            dbc.NavbarBrand("COVID-19 Dashboard", className="ms-2"),
                        ),
                        # Second column with additional text
                        dbc.Col(
                            html.Span("by Ahmed Awny", style={'color': '#add8e6', 'font-size': 'small', 'margin-left': '10px'}),
                            className="align-self-center",
                        ),
                    ],
                    align="center",  # Align the content of the row to the center
                    className="g-0",  # Set the gutter to 0 for the row
                ),
                # Navbar toggler for responsiveness
                dbc.NavbarToggler(id="navbar-toggler"),
                # Collapsible content for the navbar
                dbc.Collapse(
                    dbc.Nav(
                        [dbc.NavItem(dbc.NavLink("Home", href="/"))],  # Navigation link to the home page
                        className="ms-auto",  # Align the nav items to the right
                        navbar=True,
                    ),
                    id="navbar-collapse",
                    navbar=True,
                ),
            ],
        ),
        color="primary",  # Set the color of the navbar to primary
        dark=True,  # Use dark theme for the navbar
    )
    return navbar  # Return the navbar component
