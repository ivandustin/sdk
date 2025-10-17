from os import environ
from sys import argv
from streamlit import set_page_config, number_input, plotly_chart, cache_data
from numpy import loadtxt, unique, max
from plotly.express import bar

filepath = argv[1]
digits = int(environ.get("DIGITS", "4"))
margin = float(environ.get("MARGIN", "0.01"))
set_page_config(layout="wide")
items = cache_data(loadtxt)(filepath, ndmin=1)
x, y = cache_data(unique)(items, return_counts=True)
value = number_input("Value", value=x[0], step=10**-digits, format=f"%0.{digits}f")
minimum = value - margin
maximum = value + margin
index = (x >= minimum) & (x <= maximum)
x, y = x[index], y[index]
figure = bar(x=x, y=y)
figure.add_shape(
    type="line",
    x0=value,
    y0=0,
    x1=value,
    y1=max(y),
    line=dict(color="orange", dash="dot"),
)
figure.update_layout(autosize=True)
plotly_chart(figure)
