from sys import stdin
from streamlit import set_page_config, cache_data, plotly_chart
from plotly.express import line
from numpy import loadtxt

set_page_config(layout="wide")
values = cache_data(lambda: loadtxt(stdin, dtype=float))()
figure = line(y=values)
plotly_chart(figure)
