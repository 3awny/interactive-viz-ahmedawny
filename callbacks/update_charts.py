from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import pycountry
import pycountry_convert as pc

# Load the data
df = pd.read_csv('./data/worldometer_coronavirus_daily_data.csv')

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
    def update_charts(selected_options):
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
            if option in df['continent'].unique() or option == 'ALL':
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
