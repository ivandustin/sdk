from sys import argv
from streamlit import set_page_config, cache_data, text_input, plotly_chart
from plotly.express import bar
from numpy import loadtxt

filepath = argv[1]
set_page_config(layout="wide")
array = cache_data(loadtxt)(filepath, dtype=str, ndmin=2)
x, y = array[:, 1], list(map(float, array[:, 0]))
highlight = text_input("Highlight")
figure = bar(x=x, y=y)
if highlight:
    figure.add_shape(
        type="line",
        x0=highlight,
        y0=0,
        x1=highlight,
        y1=max(y),
        line=dict(color="orange", dash="dot"),
    )
plotly_chart(figure)
