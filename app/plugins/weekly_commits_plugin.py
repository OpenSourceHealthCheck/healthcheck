__author__ = 'clyde'

from stats_plugin import stats
import numpy as np

class weekly_commits(stats):


    def __init__(self, *args, **kwargs):

        self.figs = {}
        stats.__init__(self, *args, **kwargs)

    def gen_data(self):
        raise NotImplementedError

    def gen_figs(self):
        raise NotImplementedError

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