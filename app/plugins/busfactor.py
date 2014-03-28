from html_provider_base import html_provider_base
import numpy as np

class busfactor(html_provider_base):
    
    def __init__(self):
        html_provider_base.__init__(self)
    
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
        busfactor = useful.sum()
        content = "The <a href='http://en.wikipedia.org/wiki/Bus_factor'>bus factor</a> for this code is approximately %i over all time<br>" %(busfactor)
        
        comarray = np.array(commits)[0:52]
        useful = (comarray > comarray.mean())
        busfactor = useful.sum()
        
        content += "The bus factor in the last year is approximately %i" % (busfactor)
        
        if busfactor > 1:
            self.passes = True
        html = self.div % content
        return html

