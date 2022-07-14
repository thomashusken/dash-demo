"""
Main Dash app
"""
from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
from flask import Flask

df = pd.read_csv(
    "https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/"
    "a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv"
)


def register_dash(app: Flask) -> Dash:
    """
    Register the Dash app with the Flask server
    :param app: Flask app
    :return: a Dash app
    """

    dash = Dash(__name__, server=app, url_base_pathname="/gapminder/", serve_locally=True)

    fig = px.scatter(
        df,
        x="gdp per capita",
        y="life expectancy",
        size="population",
        color="continent",
        hover_name="country",
        log_x=True,
        size_max=60,
    )

    dash.layout = html.Div(
        [
            html.Div(
                [
                    html.H4(
                        "Mind the gap",
                        style={
                            "fontWeight": "bold",
                            "fontFamily": "sans-serif",
                        },
                    ),
                    html.P(
                        "Look at all this beautiful data",
                        style={
                            "fontFamily": "sans-serif",
                        },
                    ),
                ]
            ),
            dcc.Graph(id='life-exp-vs-gdp', figure=fig),
        ]
    )
    return dash
