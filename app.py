import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables ######

myheading = "Social Media Usage"
mytitle = "Number of Active Users - In Millions"
x_values = ['2013', '2014', '2015', '2016', '2017', '2018']
y1_values = [150, 300, 400, 600, 800, 1000]
y2_values = [201, 208, 219, 231, 239, 242]
y3_values = [50, 71, 107, 158, 187, 187]
color1 = '#eb4034' 
color2 = '#4287f5'
color3 = '#e5eb34'
name1 = 'Instagram'
name2 = 'Facebook'
name3 = 'Snapchat'
tabtitle = 'Social Media Apps'
sourceurl = 'https://www.statista.com/statistics/253577/number-of-monthly-active-instagram-users/'
githublink = 'https://github.com/ktemsupa/dash-linechart-example'

########### Set up the chart

# create traces
trace0 = go.Scatter(
    x = x_values,
    y = y1_values,
    mode = 'lines',
    marker = {'color': color1},
    name = name1
)
trace1 = go.Scatter(
    x = x_values,
    y = y2_values,
    mode = 'lines',
    marker = {'color': color2},
    name = name2
)
trace2 = go.Scatter(
    x = x_values,
    y = y3_values,
    mode = 'lines',
    marker = {'color': color3},
    name = name3
)

# assign traces to data
data = [trace0, trace1, trace2]
layout = go.Layout(
    title = mytitle
)

# Generate the figure dictionary
fig = go.Figure(data=data,layout=layout)

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H2(
        children=myheading,
        style={'textAlign':'center'}
    ),
    dcc.Graph(
        id='figure-1',
        figure=fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()
