import app.utils.html_provider as html_provider
import numpy as np

class busfactor(html_provider.html_provider_base):

    priority = 10
    
    def get_html(self, repo):
        '''
        Checks if a README file exists
        '''

        it = repo.iter_contributor_statistics()
        commits = []
        for con in it:
            commits.append(sum([w['c'] for w in con.weeks]));

        comarray = np.array(commits)
        useful = (comarray >= comarray.mean())
        busfactor = useful.sum()
        content = "The <a href='http://en.wikipedia.org/wiki/Bus_factor'>bus factor</a> for this code is approximately %i over all time<br>" %(busfactor)
        
        comarray = np.array(commits)[0:52]
        useful = (comarray >= comarray.mean())
        busfactor = useful.sum()
        
        content += "The bus factor in the last year is approximately %i" % (busfactor)
        
        if busfactor > 1:
            self.passes = True
        html = self.div % content
        return html

