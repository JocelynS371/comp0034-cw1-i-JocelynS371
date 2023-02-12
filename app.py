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
    df['Latitude'] = round(df['Latitude'], 2)
    df['Longitude'] = round(df['Longitude'], 2)
    return df
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

df=read_df()
grouped = df.groupby(['Longitude', 'Latitude'])
temp_plot_fig=temp_plot(df)
print(len(temp_plot_fig))
line_temp=px.line(
    df,
    x='Date',
    y='Temperture',
    template='simple_white')

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout=dbc.Container(children=[
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
                figure=temp_plot_fig['fig_1'])]),
        ])
            
    ]
)
@app.callback(
    Output(component_id='temp_line', component_property='figure'),
    [Input(component_id='figure-dropdown', component_property='value')]
)
def update_figure(selected_value):
    figures = temp_plot(df)
    return figures[selected_value]

if __name__=='__main__':
    app.run_server(debug=True)