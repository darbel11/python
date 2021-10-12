import os
from pathlib import Path

import pandas
import matplotlib.pyplot as plot
from scipy import stats

script_directory = os.path.dirname(os.path.abspath(__file__))
source_file = str(script_directory) + "\\source_file.csv"

data = pandas.read_csv(str(source_file))
data["measurement_value"].plot(kind="bar")

data_frame = pandas.DataFrame(data={
    "value": data["measurement_value"]
})

print(stats.kstest(data_frame["value"],
                   "norm",
                   (data_frame["value"].mean(), data_frame["value"].std()),
                   N=len(data_frame["value"])
                   ))
# Кажется, распределние близко к нормальному, т.к P-значение велико
