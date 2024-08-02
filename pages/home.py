from dash import dcc
from dash import html
from dash import register_page

register_page(__name__, name='Home', top_nav=True, path='/')

file_path = 'pages/countries_list.txt'
with open(file_path, 'r') as file:
    countries_list = file.read().splitlines()

country_options = [{'label': country, 'value': country} for country in countries_list]
# Add options for continents and 'All Countries'
country_options.extend([
    {'label': 'All Countries', 'value': 'ALL'},
    {'label': 'Africa', 'value': 'Africa'},
    {'label': 'Asia', 'value': 'Asia'},
    {'label': 'Europe', 'value': 'Europe'},
    {'label': 'North America', 'value': 'North America'},
    {'label': 'South America', 'value': 'South America'},
    {'label': 'Oceania', 'value': 'Oceania'}
])

# Include the Bootstrap CSS
external_stylesheets = ['https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css']

def layout():
    return html.Div([
        dcc.Location(id='url', refresh=False),
        html.H1("COVID-19 Dashboard", style={'text-align': 'center'}),
        html.Div([
            html.H2("Select Countries/Continents/All"),
            dcc.Dropdown(
                id='country-dropdown',
                options=country_options,
                value=['USA'],
                multi=True
            )
        ], style={'margin-left': '220px', 'padding': '20px'}),
        html.Div(id='graphs', children=[
            html.Div([
                html.H2(id='introduction', children="Introduction"),
                html.P("Brief introduction about the COVID-19 dashboard and its purpose."),
            ], style={'margin-left': '220px', 'padding': '20px'}),
            html.Div([
                html.H2(id='overview', children="Overview"),
                html.P("This section provides an overview of the total and new COVID-19 cases and deaths."),
            ], id='overview', style={'padding-top': '50px', 'margin-left': '220px'}),
            html.Div([
                dcc.Graph(id='total-cases-graph')
            ], id='total-cases', style={'padding-top': '50px', 'margin-left': '220px'}),
            html.Div([
                dcc.Graph(id='total-deaths-graph')
            ], id='total-deaths', style={'padding-top': '50px', 'margin-left': '220px'}),
            html.Div([
                dcc.Graph(id='new-cases-graph')
            ], id='new-cases', style={'padding-top': '50px', 'margin-left': '220px'}),
            html.Div([
                dcc.Graph(id='new-deaths-graph')
            ], id='new-deaths', style={'padding-top': '50px', 'margin-left': '220px'}),
            html.Div([
                dcc.Graph(id='active-cases-graph')
            ], id='active-cases', style={'padding-top': '50px', 'margin-left': '220px'}),
            html.Div([
                dcc.Graph(id='deaths-percentage-graph')
            ], id='deaths-percentage', style={'padding-top': '50px', 'margin-left': '220px'}),
        ])
    ])
