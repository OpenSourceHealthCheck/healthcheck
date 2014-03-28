__author__ = 'clyde'
import numpy as np
import plotly
from html_provider_base import html_provider_base

plotly_usrn, plotly_secret = 'Clyde', "1nq387dk20"

class stats(html_provider_base):

    def __init__(self, *args, **kwargs):

        self.figs = {}
        html_provider_base.__init__(self, *args, **kwargs)

    def gen_data(self):
        raise NotImplementedError

    def gen_figs(self):
        raise NotImplementedError

    def gen_bar(self, title, dataset):
        """Generates a plotly barchart from the dataset

        Returns plotly object of the form:

        {'url':'', 'filename': '', 'error': 'No data', 'warning': '', 'message': ''}"""

        if not any(dataset):
            return {'url':'', 'filename': 'title', 'error': 'No data', 'warning': '', 'message': ''}

        py = plotly.plotly(plotly_usrn, plotly_secret)
        data = {'x': dataset,'type': 'histogramx'}

        l = {'autosize': False,'width': 600, 'height': 400, 'showlegend': False, 'title':title}

        return py.plot([data], layout=l)

    def get_html(self, github_repo):
        '''
        Returns IFrame for a weekly commits figure
        '''

        if not self.figs.get('weekly_commits'):
            raise RuntimeError

        raw_fig_address = self.figs['weekly_commits']['url']
        content = '''<iframe id="igraph" src={fig_address} width="400" height="250" seamless="seamless" scrolling="no"></iframe>'''.format(fig_address=raw_fig_address)

        html = self.div % content
        return html

if __name__ == '__main__':
    dummy_commits = np.random.randint(10, size=100)

    test_stats = stats()
    print(test_stats.gen_bar('test_plot', dummy_commits)['url'])