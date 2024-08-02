from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import pycountry
import pycountry_convert as pc

# Load the data
df = pd.read_csv('./data/worldometer_coronavirus_daily_data.csv')

# Helper function to get continent from country name
def get_continent(country_name):
    try:
        country_alpha2 = pycountry.countries.lookup(country_name).alpha_2
        continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
        continent_name = pc.convert_continent_code_to_continent_name(continent_code)
        return continent_name
    except (LookupError, KeyError):
        return None

# Add continent column to the dataframe
df['continent'] = df['country'].apply(get_continent)

def register_callbacks(app):
    @app.callback(
        [
            Output('total-cases-graph', 'figure'),
            Output('total-deaths-graph', 'figure'),
            Output('new-cases-graph', 'figure'),
            Output('new-deaths-graph', 'figure'),
            Output('active-cases-graph', 'figure'),
            Output('deaths-percentage-graph', 'figure')
        ],
        [Input('country-dropdown', 'value')]
    )
    def update_country_graphs(selected_options):
        traces = {key: [] for key in [
            'total_cases', 'total_deaths', 'new_cases', 'new_deaths', 'active_cases', 'deaths_percentage'
        ]}

        for option in selected_options:
            if option == 'ALL':
                selected_df = df
                name = 'World'
            elif option in df['continent'].unique():
                selected_df = df[df['continent'] == option]
                name = option
            else:
                selected_df = df[df['country'] == option]
                name = option

            selected_df = selected_df.copy()  # Create a copy of the DataFrame to avoid the SettingWithCopyWarning
            selected_df['date'] = pd.to_datetime(selected_df['date'])
            selected_df = selected_df.sort_values('date')

            # Aggregate data for continents
            if option in df['continent'].unique():
                aggregated_df = selected_df.groupby('date').sum().reset_index()
            else:
                aggregated_df = selected_df

            # Calculate deaths as a percentage of total cases
            aggregated_df['deaths_percentage'] = (aggregated_df['cumulative_total_deaths'] / aggregated_df['cumulative_total_cases']) * 100

            traces['total_cases'].append(go.Scatter(
                x=aggregated_df['date'], y=aggregated_df['cumulative_total_cases'], mode='lines', name=name
            ))

            traces['total_deaths'].append(go.Scatter(
                x=aggregated_df['date'], y=aggregated_df['cumulative_total_deaths'], mode='lines', name=name
            ))

            traces['new_cases'].append(go.Scatter(
                x=aggregated_df['date'], y=aggregated_df['daily_new_cases'], mode='lines', name=name
            ))

            traces['new_deaths'].append(go.Scatter(
                x=aggregated_df['date'], y=aggregated_df['daily_new_deaths'], mode='lines', name=name
            ))

            traces['active_cases'].append(go.Scatter(
                x=aggregated_df['date'], y=aggregated_df['active_cases'], mode='lines', name=name
            ))

            traces['deaths_percentage'].append(go.Scatter(
                x=aggregated_df['date'], y=aggregated_df['deaths_percentage'], mode='lines', name=name
            ))

        return (
            {'data': traces['total_cases'], 'layout': go.Layout(title='Total Cases Over Time')},
            {'data': traces['total_deaths'], 'layout': go.Layout(title='Total Deaths Over Time')},
            {'data': traces['new_cases'], 'layout': go.Layout(title='New Cases Over Time')},
            {'data': traces['new_deaths'], 'layout': go.Layout(title='New Deaths Over Time')},
            {'data': traces['active_cases'], 'layout': go.Layout(title='Active Cases Over Time')},
            {'data': traces['deaths_percentage'], 'layout': go.Layout(title='Total Deaths as Percentage of Total Cases Over Time')}
        )
