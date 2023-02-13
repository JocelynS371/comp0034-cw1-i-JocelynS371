from dash import Dash,html,dcc, Input, Output
from xlrd import xldate_as_datetime as date_convert
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
    return df

def seperate_location(df):
    df['Latitude'] = round(df['Latitude'], 1)
    df['Longitude'] = round(df['Longitude'], 1)
    grouped = df.groupby(['Longitude', 'Latitude'])
    return grouped

def map_plot(df,option):
    #map plot to show locations
    fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude', 
                            color='Temperture', size='Temperture',
                            color_continuous_scale='Viridis',
                            size_max=15, zoom=6,
                            title='Mean Temperture in 6 locations')
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
                        options=['Temperture'],
                        value='Temperture'
                    )]),
                dbc.Col(width=9, children=[
                    html.H2(children='Map Location'),
                    dcc.Graph(
                    id='map',
                    figure=map_plot(df,'Temperture'))])])])
    return tab

def temp_plot(df):
    figures = {}
    for i, (name, group) in enumerate(grouped):
        fig = px.scatter(
            group,
            x='Date',
            y='Temperture',
            template='simple_white')
        title = f"Longitude: {name[0]} Latitude: {name[1]}"
        fig.update_layout(title=title)
        figures[f"fig_{i + 1}"] = fig
    return figures

def temp_tab(temp_plot_fig):
    tab=dbc.Container(
        children=[
            html.Div(),
            html.H1(children='Data Dashboard', className="display-1"),
            dbc.Row([
                dbc.Col(width=3, children=[
                    html.H4('select location'),
                    dcc.Dropdown(
                        id='figure-dropdown',
                        options=[{'label': f'Location {i+1}', 'value': f'fig_{i+1}'} 
                        for i in range(len(temp_plot_fig))],
                        value='fig_1'
                    )]),
                dbc.Col(width=9, children=[
                    html.H2(children='Graph of temperture change with time'),
                    dcc.Graph(
                    id='temp_line',
                    figure=temp_plot(df)['fig_1'])])])])
    return tab

df=read_df()
grouped=seperate_location(df)


app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    html.H1('Dashboard'),
    dcc.Tabs(id="tabs-graph", value='location-map', children=[
        dcc.Tab(label='location', value='location-map'),
        dcc.Tab(label='temp-time', value='temp-scatter'),
    ]),
    html.Div(id='tabs-content')
])
@app.callback(Output('tabs-content','children'),Input('tabs-graph','value'))
def content(tab):
    if tab=='location-map':
        return map_tab()
    elif tab=='temp-scatter':
        temp_plot_fig=temp_plot(df)
        return temp_tab(temp_plot_fig)

@app.callback(
    Output(component_id='temp_line', component_property='figure'),
    [Input(component_id='figure-dropdown', component_property='value')]
)
def update_figure(selected_value):
    figures = temp_plot(df)
    return figures[selected_value]

if __name__=='__main__':
    app.run_server(debug=True)