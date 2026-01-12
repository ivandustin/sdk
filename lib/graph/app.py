from sys import stdin
from streamlit import set_page_config, cache_data, plotly_chart
from plotly.express import line
from numpy import loadtxt

set_page_config(layout="wide")
array = cache_data(lambda: loadtxt(stdin, dtype=float))()
x = range(len(array)) if array.ndim == 1 else array[:, 0]
y = (array if array.ndim == 1 else array[:, 1]).astype(float)
figure = line(x=x, y=y)
plotly_chart(figure)
