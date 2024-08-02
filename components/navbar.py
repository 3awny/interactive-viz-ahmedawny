import dash_bootstrap_components as dbc
from dash import html
import dash_bootstrap_components as dbc

def create_navbar():
    navbar = dbc.Navbar(
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.NavbarBrand("COVID-19 Dashboard", className="ms-2"),
                        ),
                        dbc.Col(
                            html.Span("by Ahmed Awny", style={'color': '#add8e6', 'font-size': 'small', 'margin-left': '10px'}),
                            className="align-self-center",
                        ),
                    ],
                    align="center",
                    className="g-0",
                ),
                dbc.NavbarToggler(id="navbar-toggler"),
                dbc.Collapse(
                    dbc.Nav(
                        [dbc.NavItem(dbc.NavLink("Home", href="/"))],
                        className="ms-auto",
                        navbar=True,
                    ),
                    id="navbar-collapse",
                    navbar=True,
                ),
            ],
        ),
        color="primary",
        dark=True,
    )
    return navbar
