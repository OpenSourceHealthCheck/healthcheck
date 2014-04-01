__author__ = 'clyde'

import app.utils.stats_helper as stats_helper

class weekly_commits(stats_helper.stats):

    priority =  5

    def get_html(self, github_repo):
        '''
        Returns IFrame for a weekly commits figure
        '''

        weekly = [e['total'] for e in github_repo.iter_commit_activity()][:52]
        self.fig = self.gen_bar('Weekly commits', weekly)

        raw_fig_address = self.fig['url']
        content = '''<iframe id="igraph" src={fig_address} width="600" height="400" seamless="seamless" scrolling="no"></iframe>'''.format(fig_address=raw_fig_address)

        html = self.div % content

        if any(weekly[-10:-1]):
            self.passes = True

        return html
