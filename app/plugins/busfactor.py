import github3
from html_provider_base import html_provider_base
import numpy as np

class busfactor(html_provider_base):
    
    def get_html(self, repo):
        '''
        Checks if a README file exists
        '''

        it = repo.iter_contributor_statistics()
        commits = []
        for con in it:
            commits.append(sum([w['c'] for w in con.weeks]));

        comarray = np.array(commits)
        useful = (comarray > comarray.mean())
        
        content = "The bus factor for this code is approximatly %i" %(useful.sum())

        html = self.div % content
        return html
