# Import necessary modules from Dash dependencies and Plotly
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

# Load the data from the CSV file
df = pd.read_csv('./data/worldometer_coronavirus_daily_data.csv')

# Function to register callbacks with the Dash app
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
    # Function to update charts based on selected options from the dropdown
    def update_charts(selected_options):
        # Initialize a dictionary to hold traces for each chart
        traces = {key: [] for key in [
            'total_cases', 'total_deaths', 'new_cases', 'new_deaths', 'active_cases', 'deaths_percentage'
        ]}

        # Iterate over each selected option from the dropdown
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
            selected_df['date'] = pd.to_datetime(selected_df['date'])  # Convert the date column to datetime format
            selected_df = selected_df.sort_values('date')  # Sort the DataFrame by date

            # Aggregate data for continents or all countries
            if option in df['continent'].unique() or option == 'ALL':
                aggregated_df = selected_df.groupby('date').sum().reset_index()
            else:
                aggregated_df = selected_df

            # Calculate deaths as a percentage of total cases
            aggregated_df['deaths_percentage'] = (aggregated_df['cumulative_total_deaths'] / aggregated_df['cumulative_total_cases']) * 100

            # Add traces for each type of data to the corresponding list in the dictionary
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

        # Return the figures for each graph
        return (
            {
                'data': traces['total_cases'],
                'layout': go.Layout(
                    title='Total Cases Over Time',
                    xaxis={'title': {'text': 'Date', 'standoff': 20}},
                    yaxis={'title': {'text': 'Total Cases', 'standoff': 20}}
                )
            },
            {
                'data': traces['total_deaths'],
                'layout': go.Layout(
                    title='Total Deaths Over Time',
                    xaxis={'title': {'text': 'Date', 'standoff': 20}},
                    yaxis={'title': {'text': 'Total Deaths', 'standoff': 20}}
                )
            },
            {
                'data': traces['new_cases'],
                'layout': go.Layout(
                    title='New Cases Over Time',
                    xaxis={'title': {'text': 'Date', 'standoff': 20}},
                    yaxis={'title': {'text': 'New Cases', 'standoff': 20}}
                )
            },
            {
                'data': traces['new_deaths'],
                'layout': go.Layout(
                    title='New Deaths Over Time',
                    xaxis={'title': {'text': 'Date', 'standoff': 20}},
                    yaxis={'title': {'text': 'New Deaths', 'standoff': 20}}
                )
            },
            {
                'data': traces['active_cases'],
                'layout': go.Layout(
                    title='Active Cases Over Time',
                    xaxis={'title': {'text': 'Date', 'standoff': 20}},
                    yaxis={'title': {'text': 'Active Cases', 'standoff': 20}}
                )
            },
            {
                'data': traces['deaths_percentage'],
                'layout': go.Layout(
                    title='Total Deaths as Percentage of Total Cases Over Time',
                    xaxis={'title': {'text': 'Date', 'standoff': 20}},
                    yaxis={'title': {'text': 'Percentage', 'standoff': 20}}
                )
            }
        )
