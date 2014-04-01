__author__ = 'clyde'

import plotly
import app.utils.html_provider as html_provider

plotly_usrn, plotly_secret = "opensourcehealthcheck", "5qw88y2uov"

class stats(html_provider.html_provider_base):

    def gen_bar(self, title, dataset):
        """Generates a plotly barchart from a dataset

        Returns plotly object of the form:

        {'url':'', 'filename': '', 'error': 'No data', 'warning': '', 'message': ''}"""

        if not any(dataset):
            return {'url':'', 'filename': 'title', 'error': 'No data', 'warning': '', 'message': ''}

        py = plotly.plotly(plotly_usrn, plotly_secret)
        py.ioff()
        data = {'x': list(range(len(dataset))), 'y':dataset, 'type': 'bar'}

        l = {'autosize': True, 'width': 900, 'height': 600, 'showlegend': False, 'title':title}

        return py.plot([data], layout=l)
