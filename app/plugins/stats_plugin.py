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
        py.ioff()
        data = {'x': dataset,'type': 'bar'}
        
        l = {'autosize': True, 'width': 900, 'height': 600, 'showlegend': False, 'title':title}

        return py.plot([data], layout=l)