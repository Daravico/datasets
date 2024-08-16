from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px

app = Dash()

app.layout = html.Div([
    dcc.Graph(id="graph"),

    dcc.Interval(
        id = "interval",
        interval=1*1000,
        n_intervals=0
    )
])

@app.callback(
        Output('graph', 'figure'),
        Input('interval', 'n_intervals')
)
def update_graph(n):
    df = pd.read_csv("data_now.csv")
    fig = px.line(df.tail(), x='timestamp', y="value")
    return fig

app.run()