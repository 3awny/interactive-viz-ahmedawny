from dash import dcc
from dash import html
from dash import register_page

# Register the page with Dash
register_page(__name__, name='Home', top_nav=True, path='/')

# Read the list of countries from a file
file_path = 'pages/countries_list.txt'
with open(file_path, 'r') as file:
    countries_list = file.read().splitlines()

# Define a function to create a separator option for the dropdown
def create_separator(label):
    return {'label': label, 'value': '', 'disabled': True}

# Create options for the dropdown menu with separators
country_options = [(create_separator('All'))]
country_options.append({'label': 'All Countries', 'value': 'ALL'})
country_options.append(create_separator('Continents'))
country_options.extend([
    {'label': 'Africa', 'value': 'Africa'},
    {'label': 'Asia', 'value': 'Asia'},
    {'label': 'Europe', 'value': 'Europe'},
    {'label': 'North America', 'value': 'North America'},
    {'label': 'South America', 'value': 'South America'},
    {'label': 'Oceania', 'value': 'Oceania'}
])
country_options.append(create_separator('Countries'))
country_options.extend([{'label': country, 'value': country} for country in countries_list])

# Include the Bootstrap CSS for styling
external_stylesheets = ['https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css']

# Define the layout of the Dash application
def layout():
    return html.Div([
        dcc.Location(id='url', refresh=False),  # URL component for navigation
        html.H1("COVID-19 Dashboard", style={'text-align': 'center', 'padding': '50px'}),  # Main title
        html.Div([
            html.H2(id='overview', children="Overview"),  # Overview section header
            html.P(
                "Welcome to the COVID-19 Dashboard. This dashboard provides a detailed overview of the pandemic's impact from January 2020 to May 2022. It features interactive graphs that display the total and new COVID-19 cases and deaths over this period. You can explore the data by country and/or continent to understand the trends and patterns across different regions. The goal of these visualizations is to offer insights into the progression of the pandemic, helping you to analyze and interpret the data effectively."
            ),  # Overview text
        ], id='overview', style={'padding': '50px', 'margin-left': '50px', 'margin-right': '50px'}),
        html.Div([
            html.H2("Select Countries/Continents/All"),  # Dropdown menu header
            dcc.Dropdown(
                id='country-dropdown',  # Dropdown menu for selecting countries/continents
                options=country_options,
                value=['USA', 'Europe', 'Asia'],  # Default selected values
                multi=True  # Allow multiple selections
            )
        ], style={'padding': '50px', 'margin-left': '50px', 'margin-right': '50px'}),
        html.Div(id='graphs', children=[
            html.Div([
                dcc.Graph(id='total-cases-graph')  # Graph for total cases
            ], id='total-cases', style={'padding': '50px'}),
            html.Div([
                dcc.Graph(id='total-deaths-graph')  # Graph for total deaths
            ], id='total-deaths', style={'padding': '50px'}),
            html.Div([
                dcc.Graph(id='new-cases-graph')  # Graph for new cases
            ], id='new-cases', style={'padding': '50px'}),
            html.Div([
                dcc.Graph(id='new-deaths-graph')  # Graph for new deaths
            ], id='new-deaths', style={'padding': '50px'}),
            html.Div([
                dcc.Graph(id='active-cases-graph')  # Graph for active cases
            ], id='active-cases', style={'padding': '50px'}),
            html.Div([
                dcc.Graph(id='deaths-percentage-graph')  # Graph for deaths percentage
            ], id='deaths-percentage', style={'padding': '50px'}),
        ]),
        html.Div([
            html.P("Acknowledgements: created using Dash"),
            html.A("Dash website", href="https://dash.plotly.com", target="_blank"),  # Link to Dash website
            html.Br(),
        ], style={'text-align': 'center', 'padding': '50px'}),
        html.Div([
            html.P("GitHub"),
            html.A("GitHub repo", href="https://github.com/3awny/interactive-viz-ahmedawny", target="_blank")  # Link to GitHub repository
        ], style={'text-align': 'center', 'padding': '20px'})
    ])
