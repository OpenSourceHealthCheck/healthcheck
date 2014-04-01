import github3
from app.plugins.html_provider_base import html_provider_base

class is_my_code_ready(html_provider_base):
    
    def get_html(self, github_repo):
        '''
        Simple Implementation for testing
        '''
        content = "%s is ready to share :)  <a href='http://shouldisharemyco.de#%s'>Check this on ShouldIShareMyCo.de</a>" % (github_repo.name,github_repo.git_url)
        html = self.div % content
        self.passes = True

        return html
