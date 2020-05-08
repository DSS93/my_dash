import dash
import dash_core_components as dcc
import dash_html_components as html
import requests
from dash.dependencies import Input, Output
import plotly.graph_objects as go


url = 'https://api.rootnet.in/covid19-in/stats/latest'
response = requests.get(url).json()
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'DS DASH'
server = app.server


def total_india():
    data = response['data']['summary']
    return data


def state_loc():
    data = response['data']['regional']
    loc = [data['loc'] for data in data]
    return loc


def state_total_confirmed():
    data = response['data']['regional']
    total_confirmed = [d['totalConfirmed'] for d in data]
    return total_confirmed


def state_total_discharge():
    data = response['data']['regional']
    total_discharge = [d['discharged'] for d in data]
    return total_discharge


def state_total_death():
    data = response['data']['regional']
    total_deaths = [d['deaths'] for d in data]
    return total_deaths


def state_total_confirmed_foreign():
    data = response['data']['regional']
    total_foreign = [d['confirmedCasesForeign'] for d in data]
    return total_foreign


def pie_county_total():
    total = response['data']['summary']['total']
    return total


def pie_county_recovered():
    discharge = response['data']['summary']['discharged']
    return discharge


def pie_county_death():
    death = response['data']['summary']['deaths']
    return death


def state_loc_name():
    data = response['data']['regional']
    loc = [data['loc'] for data in data]
    options = [{'label': name, 'value': name} for name in loc]
    return options


def pie_all_state_case(total):
    data = response['data']['regional']
    data = list(filter(lambda data : data['loc'] == total, data))
    return data[0]['confirmedCasesIndian']


def pie_all_state_recovered(recover):
    data = response['data']['regional']
    data = list(filter(lambda data : data['loc'] == recover, data))
    return data[0]['discharged']


def pie_all_state_death(death):
    data = response['data']['regional']
    data = list(filter(lambda data : data['loc'] == death, data))
    return data[0]['deaths']


labels = ['Total', 'Death', 'Recovered']
values = [pie_county_total(),  pie_county_death(), pie_county_recovered()]
colors = ['#3498DB', '#E74C3C', '#2ECC71']
fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=15, marker=dict(colors=colors))
fig.update_layout(title='Country Data')


app.layout = html.Div(children=[
    html.H1(children='DS Data Visualization Covid-19 for INDIA', style={'text-align': 'center', 'color': 'blue'}),


    dcc.Dropdown(
        id='my_dropDown',
        options=state_loc_name(),
        value='Delhi',
        multi=False,
        clearable=False,
        style={"width": "50%"}
    ),


    dcc.Graph(
        id='the_graph'
    ),

    dcc.Graph(
        id='pie-country-data',
        figure=fig
    ),


    dcc.Graph(
        id='india-data',
        figure={
            'data':[
                {'x': list(total_india().keys()), 'y': list(total_india().values()), 'type': 'bar', 'name': 'SF'},
            ],
            'layout': {
                'title': 'Covid-19 Total Cases',
            }
        }
    ),

    dcc.Graph(
        id='state-total-case',
        figure={
            'data': [
                {'x': state_loc(), 'y': state_total_confirmed(),
                 'type': 'bar', 'name': 'SF'},
            ],
            'layout': {
                'title': 'State Wise Covid-19 Cases'
            }
        }
    ),


    dcc.Graph(
        id='recovered-graph',
        figure={
            'data': [
                {'x': state_loc(), 'y': state_total_discharge(), 'type': 'bar', 'name': 'SF'},
            ],
            'layout': {
                'title': 'State wise Covid-19 Recovered Data'
            }
        }
    ),
    dcc.Graph(
        id='death-graph',
        figure={
            'data': [
                {'x': state_loc(), 'y': state_total_death(), 'type': 'bar', 'name': 'SF'},
            ],
            'layout': {
                'title': 'State wise Covid-19 Deaths Data'
            }
        }
    ),

    dcc.Graph(
        id='foreign-graph',
        figure={
            'data': [
                {'x': state_loc(), 'y': state_total_confirmed_foreign(), 'type': 'bar', 'name': 'SF'},
            ],
            'layout': {
                'title': 'State wise Covid-19 Foreign Cases'
            }
        }
    ),
])


@app.callback(
    Output(component_id='the_graph', component_property='figure'),
    [Input(component_id='my_dropDown', component_property='value')])
def update_graph(my_dropDown):
    values1 = [pie_all_state_case(my_dropDown), pie_all_state_death(my_dropDown), pie_all_state_recovered(my_dropDown)]
    fig_state = go.Figure(data=[go.Pie(labels=labels, values=values1)])
    fig_state.update_traces(hoverinfo='label+value', textfont_size=15, marker=dict(colors=colors))
    fig_state.update_layout(title='State Wise Data')
    return fig_state


def update_graph1(my_dropDown):
    values1 = [pie_all_state_case(my_dropDown), pie_all_state_death(my_dropDown), pie_all_state_recovered(my_dropDown)]
    fig_state = go.Figure(data=[go.Pie(labels=labels, values=values1)])
    fig_state.update_traces(hoverinfo='label+value', textfont_size=15, marker=dict(colors=colors))
    fig_state.update_layout(title='State Wise Data')
    return fig_state


if __name__ == '__main__':
    app.run_server()
