from datetime import datetime
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
from dash import Dash,html,dcc, Input, Output



def read_df():

    """return a renamed dataframe"""

    data_path='data_set_prepared.csv'
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
    """ seperate location into a groupby object"""

    df['Latitude'] = round(df['Latitude'], 1)
    df['Longitude'] = round(df['Longitude'], 1)
    grouped = df.groupby(['Longitude', 'Latitude'])
    return grouped


def map_plot(df,option):
    """create a scatter plot on a map"""

    fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude',
                            color=f'{option}', size=f'{option}',
                            template='seaborn',
                            color_continuous_scale='Viridis',
                            size_max=15, zoom=6,
                            title=f'Mean {option} in 6 locations',
                            hover_data=['Latitude','Longitude'])
    fig.update_layout(mapbox_style='open-street-map')
    return fig


def stat_card(grouped, option,locat):
    """
    grouped: grouped data
    option: the variable to show
    locat: turple of coordinate
    """

    mean=round(grouped.mean()[option][locat],2)
    std=round(grouped.std()[option][locat],2)
    box = dbc.Card(className="bg-dark text-light", children=[
        dbc.CardBody([
            html.H4(location_2[f'{locat}'], id="card-name", className="card-title"),
            html.Br(),
            html.H6(f"Mean of:{option} at {location_2[f'{locat}']}", className="card-title"),
            html.H4(mean, className="card-text text-light"),
            html.Br(),
            html.H6(f"Standard Deviation of:{option} at {location_2[f'{locat}']}", className="card-title"),
            html.H4(std, className="card-text text-light"),
            html.Br()
        ])
    ])
    return box


def map_tab():
    """create a tab for the map graph"""

    tab=dbc.Container(
        children=[
            html.Div(),
            dbc.Row([
                dbc.Col(width=3, children=[
                    html.H2('Select'),
                    dcc.Dropdown(
                        id='select',
                        options=[{'label':f'{option}','value':f'{option}'}
                        for option in df.columns],
                        value='Temperture'
                    ),
                    dcc.Dropdown(
                        id='select-locat',
                        options=location_2,
                        value=(-36.7, 63.6)
                    ),
                    html.Br(),
                    html.Div(id='stats-card',children=stat_card(grouped,'Temperture',(-36.6, 63.6)))
                    ]),
                dbc.Col(width=9, children=[
                    html.H2(children='Map Location'),
                    dcc.Graph(
                    id='map',
                    figure=map_plot(df,'Temperture'))])])])
    return tab


def time_plot(df, optionx,optiony,trend):
    """create a scatter plot"""

    figures = {}
    grouped = df.groupby(['Longitude', 'Latitude'])
    for i, (name, group) in enumerate(grouped):
        if trend == 'none':
            fig = px.scatter(
                group,
                x=optionx,
                y=optiony,
                template='seaborn')
        elif trend in trend_option:
            fig = px.scatter(
                group,
                x=optionx,
                y=optiony,
                template='seaborn',
                trendline=trend)
        title = f"{optiony} varying with {optionx} where Longitude= {name[0]} Latitude= {name[1]}"
        fig.update_layout(title=title)
        figures[f"fig_{i + 1}"] = fig
    return figures


def time_tab(time_plot_fig):
    """create a tab for the scatter graph"""

    tab = dbc.Container(
        children=[
            html.Div(),
            html.H3(children='Scatter graph to show relations'),
            dbc.Row([
                html.Div(children=[
                html.H5('Select Variable to show on y axis:'),
                dcc.RadioItems(
                        id='radio-option-y',
                        options=[{'label': f'{option}', 'value': f'{option}'}
                        for option in df.columns],
                        value='Temperture',),
                html.H5('Select Variable to show on x axis:'),
                dcc.RadioItems(
                        id='radio-option-x',
                        options=[{'label': f'{option}', 'value': f'{option}'}
                        for option in df.columns],
                        value='Date')]),
                dbc.Col(width=6, children=[
                    html.H5('Select location'),
                    dcc.Dropdown(
                        id='dropdown-location',
                        options=[{'label': f'Location {i+1}', 'value': f'fig_{i+1}'}
                        for i in range(len(time_plot_fig))],
                        value='fig_1')]),
                dbc.Col(width=6,children=[
                    html.H5(children='Select trendline option'),
                    dcc.Dropdown(
                                id='dropdown-trend',
                                options=[{'label': f'{option}', 'value': f'{option}'}
                                            for option in trend_option],
                                value='none')]
                    ),
                    ]),

                dbc.Col(width=12, children=[
                    dcc.Graph(
                    id='time_scatter',
                    figure=time_plot_fig['fig_1'])
                ])
                ])
    return tab


df=read_df()
grouped=seperate_location(df)
location={}
location_2={}
for i, (name, group) in enumerate(grouped):
    location_2[f'{name}']=f'location {i+1}'
    location[f'location {i+1}']=name
trend_option=['none','ols', 'lowess', 'expanding']
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = html.Div([
    html.H1('Data Dashboard for Angmagssalik Array in the Denmark Strait Overflow - 1998 to 2015'),
    dcc.Tabs(id="tabs-graph", value='location-map',
     children=[
        dcc.Tab(label='Map Plot', value='location-map'),
        dcc.Tab(label='Scatter Graphs', value='time-scatter')
    ]),
    html.Div(id='tabs-content')
])

#callback for tabs
@app.callback(Output('tabs-content','children'),Input('tabs-graph','value'))
def content(tab):
    if tab=='location-map':
        return map_tab()
    if tab=='time-scatter':
        time_plot_fig=time_plot(df,'Date','Temperture','none')
        return time_tab(time_plot_fig)



# Callback for time
@app.callback(
    Output(component_id='time_scatter', component_property='figure'),
    Input(component_id='dropdown-location', component_property='value'),
    Input(component_id='radio-option-x', component_property='value'),
    Input(component_id='radio-option-y', component_property='value'),
    Input(component_id='dropdown-trend', component_property='value')
)
def update_figure(location_value, radio_option_x,radio_option_y,trend):
    figures = time_plot(df, radio_option_x,radio_option_y,trend)
    return figures[location_value]


# Callback for map
@app.callback(
    Output(component_id='map', component_property='figure'),
    [Input(component_id='select', component_property='value')]
)
def update_figure(option):
    return map_plot(df, option)


@app.callback(
    Output("stats-card", "children"),
    [Input(component_id='select', component_property='value'),
    Input(component_id='select-locat', component_property='value')]
    )
def render_stats_panel(option,locat):
    return stat_card(grouped,option,eval(locat))


if __name__=='__main__':
    app.run_server(debug=True)
