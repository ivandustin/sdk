from sys import stdin
from streamlit import set_page_config, cache_data, text_input, plotly_chart
from plotly.express import bar
from numpy import loadtxt

set_page_config(layout="wide")
array = cache_data(lambda: loadtxt(stdin, dtype=str))()
x = range(len(array)) if array.ndim == 1 else array[:, 0]
y = (array if array.ndim == 1 else array[:, 1]).astype(float)
highlight = text_input("Highlight")
figure = bar(x=x, y=y)
if highlight:
    figure.add_shape(
        type="line",
        x0=highlight,
        y0=0,
        x1=highlight,
        y1=y.max(),
        line={"color": "orange", "dash": "dot"},
    )
plotly_chart(figure)
