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
df=read_df()
def seperate_location(df):
    
    return df
df=read_df()

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
                    id='location-select',
                    options=['A','B'],
                    value='A'
                )]),
            dbc.Col(width=9, children=[
                html.H2(children='graph of temperture change with time'),
                dcc.Graph(
                id='temp_line',
                figure=line_temp)]),
        ])
            
    ]
)

if __name__=='__main__':
    app.run_server(debug=True)