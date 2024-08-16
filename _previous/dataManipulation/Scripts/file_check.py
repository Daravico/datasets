from dash import Dash, html, dcc, Input, Output, callback, State
import pandas as pd
import plotly.express as px
import sqlite3
import threading
import serial
from datetime import datetime


try: 
    ser = serial.Serial('COM12', 9600)
except:
    print("Error")


conn = sqlite3.connect("6_data3.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS sensor_data (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               timestamp TEXT,
               value1 INTEGER,
               value2 INTEGER
               )
               ''')
conn.commit()

cursor.close()
conn.close()


def read_arduino():
    try:
        print("Starting to collect data...")
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').strip()

                values = line.split(",")

                if len(values) == 2:

                    value1 = int(values[0])
                    value2 = int(values[1])
                    timestamp = str(datetime.now())

                    try:
                        print(value1)
                        print(value2)
                        print(timestamp)
                        cursor.execute('''INSERT INTO sensor_data (timestamp, value1, value2) VALUES (?, ?, ?)''', (timestamp, value1, value2))
                        conn.commit()
                    except:
                        print("Problem storing...")
                        conn.rollback()

    except KeyboardInterrupt:
        print("Closing...")
        ser.close()


# def load_data():
#     return pd.read_csv("6_arduino_data.csv")

def load_data():
    conn = sqlite3.connect("6_data3.db")
    df = pd.read_sql_query("SELECT * FROM sensor_data", conn)
    conn.close()
    return df

app = Dash()

app.layout = html.Div([
    dcc.Interval(
        id='interval',
        interval=1*300,
        n_intervals=0
    ),
    dcc.Graph(id="graph")
])
# ----------------------------------

@callback(
        Output('graph', 'figure'),
        Input('interval', 'n_intervals')
)
def update_function(_):
    df = load_data()
    dff = df.tail(60)
    print(dff)
    fig = px.line(dff, x="timestamp", y="value1") 
    fig.add_scatter(x=dff['timestamp'], y=dff['value2'])
    return fig

# ----------------------------------

thread = threading.Thread(target=read_arduino)
thread.daemon = False
thread.start()

app.run()