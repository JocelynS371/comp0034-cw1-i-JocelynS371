from dash import Dash,html,dcc, Input, Output
from datetime import datetime
import plotly.express as px
import dash_bootstrap_components as dbc
from pathlib import Path
import pandas as pd


def read_df():

    """return a renamed dataframe"""

    #need to change column names
    # data_path= Path(__file__).parent.joinpath('data', 'data_set_prepared.csv')
    data_path='data_set_prepared.csv'
    # cols = ['Temperture', 'Salinity', 'density', 'Pressure', 'Date', 'Longitude', 'Latitude', 'Bottom Depth']
    df = pd.read_csv(data_path)
    df.rename(columns={
    'Potential_temperature_C':'Temperture',
    'Practical_salinity':'Salinity',
    'Potential_density_anomaly_kgm3':'Density',
    'Pressure_decibar':'Pressure',
    'Serial_date_number_base_date_1_January_0000':'Date',
    'Bottom_Depth_m':'Bottom Depth'
    },inplace=True)
    df['Date'] = [datetime.fromordinal(int(date)) for date in df['Date']] 
    return df

def seperate_location(df):
    df['Latitude'] = round(df['Latitude'], 1)
    df['Longitude'] = round(df['Longitude'], 1)
    grouped = df.groupby(['Longitude', 'Latitude'])
    return grouped

def map_plot(df,option):
    fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude', 
                            color=f'{option}', size=f'{option}',
                            color_continuous_scale='Viridis',
                            size_max=15, zoom=6,
                            title=f'Mean {option} in 6 locations')
    fig.update_layout(mapbox_style='open-street-map')
    return fig

def map_tab():
    tab=dbc.Container(
        children=[
            html.Div(),
            html.H1(children='Locations', className="display-1"),
            dbc.Row([
                dbc.Col(width=3, children=[
                    html.H4('Select'),
                    dcc.Dropdown(
                        id='select',
                        options=['Temperture','Salinity'],
                        value='Temperture'
                    )]),
                dbc.Col(width=9, children=[
                    html.H2(children='Map Location'),
                    dcc.Graph(
                    id='map',
                    figure=map_plot(df,'Temperture'))])])])
    return tab

def time_plot(df, option):
    figures = {}
    grouped = df.groupby(['Longitude', 'Latitude'])
    for i, (name, group) in enumerate(grouped):
        fig = px.scatter(
            group,
            x='Date',
            y=option,
            template='simple_white')
        title = f"Longitude: {name[0]} Latitude: {name[1]}"
        fig.update_layout(title=title)
        figures[f"fig_{i + 1}"] = fig
    return figures


def time_tab(time_plot_fig):
    tab = dbc.Container(
        children=[
            html.Div(),
            html.H1(children='Data Dashboard', className="display-1"),
            dbc.Row([
                dbc.Col(width=3, children=[
                    html.H4('Select Variable to show'),
                    dcc.RadioItems(
                        id='radio-option',
                        options=[
                            {'label': 'Temperture', 'value': 'Temperture'},
                            {'label': 'Salinity', 'value': 'Salinity'}
                        ],
                        value='Temperture'
                    ),
                    html.H4('select location'),
                    dcc.Dropdown(
                        id='dropdown-location',
                        options=[{'label': f'Location {i+1}', 'value': f'fig_{i+1}'} 
                        for i in range(len(time_plot_fig))],
                        value='fig_1'
                    )]),

                dbc.Col(width=9, children=[
                    html.H2(children='Graph of Temp/Salinity change with time'),
                    dcc.Graph(
                    id='time_scatter',
                    figure=time_plot_fig['fig_1'])
                ])
                    
                ])
            ])

    return tab

def comparison_plot():

    return

def comparison_tab():

    return


df=read_df()
grouped=seperate_location(df)


app = Dash(external_stylesheets=[dbc.themes.DARKLY])


app.layout = html.Div([
    html.H1('Dashboard'),
    dcc.Tabs(id="tabs-graph", value='location-map', children=[
        dcc.Tab(label='Map Plot', value='location-map'),
        dcc.Tab(label='Time Trend', value='time-scatter'),
        dcc.Tab(label='Comparision of Data', value='comparison')
    ]),
    html.Div(id='tabs-content')
])


@app.callback(Output('tabs-content','children'),Input('tabs-graph','value'))
def content(tab):
    if tab=='location-map':
        return map_tab()
    elif tab=='time-scatter':
        time_plot_fig=time_plot(df,'Temperture')
        return time_tab(time_plot_fig)
    elif tab=='comparison':
        return comparison_tab()



# Callback for time
@app.callback(
    Output(component_id='time_scatter', component_property='figure'),
    Input(component_id='dropdown-location', component_property='value'),
    Input(component_id='radio-option', component_property='value')
)
def update_figure(location_value, radio_option):
    figures = time_plot(df, radio_option)
    return figures[location_value]


# Callback for map
@app.callback(
    Output(component_id='map', component_property='figure'),
    [Input(component_id='select', component_property='value')]
)
def update_figure(option):
    return map_plot(df, option)
if __name__=='__main__':
    app.run_server(debug=True)