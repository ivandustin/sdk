from sys import argv
from streamlit import set_page_config, plotly_chart
from plotly.express import bar
from numpy import loadtxt


def main():
    xpath = argv[1]
    ypath = argv[2]
    zpath = argv[3]
    x = loadtxt(xpath, ndmin=1)
    y = loadtxt(ypath, ndmin=2)[-1]
    z = loadtxt(zpath, ndmin=2)[-1][-1]
    figure = bar(x=x, y=y)
    figure.add_shape(
        type="line",
        x0=z,
        y0=0,
        x1=z,
        y1=y.max(),
        line={"color": "orange", "dash": "dot"},
    )
    plotly_chart(figure)


if __name__ == "__main__":
    set_page_config(layout="wide")
    main()
