__author__ = 'clyde'

import plotly
from html_provider_base import html_provider_base

plotly_usrn, plotly_secret = 'Clyde', "1nq387dk20"

class stats(html_provider_base):

    def gen_bar(self, title, dataset):
        """Generates a plotly barchart from a dataset

        Returns plotly object of the form:

        {'url':'', 'filename': '', 'error': 'No data', 'warning': '', 'message': ''}"""

        if not any(dataset):
            return {'url':'', 'filename': 'title', 'error': 'No data', 'warning': '', 'message': ''}

        py = plotly.plotly(plotly_usrn, plotly_secret)
        data = {'x': dataset,'type': 'histogramx'}

        l = {'autosize': False,'width': 600, 'height': 400, 'showlegend': False, 'title':title}

        return py.plot([data], layout=l)