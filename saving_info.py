import pandas as pd
import time
import os
import numpy as np

csv_file = "data_now.csv"

if not os.path.exists(csv_file):
    df = pd.DataFrame(columns=['timestamp', 'value'])
    df.to_csv(csv_file, index=False)


while True:
    row = pd.DataFrame({
        'timestamp': [pd.Timestamp.now()],
        'value': [np.random.rand()]
    })

    row.to_csv(csv_file, mode='a', header=False, index=False)

    time.sleep(1)