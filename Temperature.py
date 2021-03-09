import pandas as pd
import plotly.figure_factory as ff
import csv
import random
import statistics

df = pd.read_csv("Average.csv")
data = df["Temperature"].tolist()
std_deviation = statistics.stdev(data)
population_mean = statistics.mean(data)


print("Population Mean:", population_mean)
print("Standard Deviation:", std_deviation)
fig = ff.create_distplot([data], ["Temperature"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0,1], mode = "line", name = "Mean"))
fig.show()