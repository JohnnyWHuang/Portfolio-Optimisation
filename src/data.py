import random

import pandas as pd

from IPython.core.display import display, HTML


def import_range(date_from=None, date_to=None):
    data = pd.read_csv("../adjusted_price_data.csv", parse_dates=True, index_col="Date")[date_from:date_to]
    min_present = (len(data) / 100) * 60
    data = data.drop([name for name, series in data.items() if len(series.unique()) <= min_present], axis=1)
    return data.fillna(method = "ffill", limit=10).fillna(method = "bfill", limit=10).dropna(axis=1)

# Create some number of portfolios with some number of stocks in each
def generate_random_portfolios(complete_portfolio, no_stocks, no_portfolios=1, random_state=0):
    return [complete_portfolio.sample(no_stocks, axis=1, random_state=portfolio + random_state) for portfolio in range(no_portfolios)]

# Output dataframes side by side for increased visibility and understandability.
# Modified from: https://stackoverflow.com/questions/38783027/jupyter-notebook-display-two-pandas-tables-side-by-side
def display_side_by_side(dataframes: list, captions: list):
    output = ""
    
    for caption, df in zip(captions, dataframes):
        output += df.style.set_table_attributes("style='display:inline'").set_caption(caption)._repr_html_()
        output += "\xa0\xa0\xa0"
    
    display(HTML(output))