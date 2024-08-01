import dash_bootstrap_components as dbc
from dash import html
import dash_bootstrap_components as dbc

def create_navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="/")),
            dbc.NavItem(dbc.NavLink("Global", href="/global")),
        ],
        brand="COVID-19 Dashboard",
        brand_href="/",
        color="primary",
        dark=True,
    )
    return navbar
