import github3
from html_provider_base import html_provider_base

class is_my_code_ready(html_provider_base):
    
    def get_html(self, github_repo):
        '''
        Simple Implementation for testing
        '''
        content = '%s is ready to share :)' % github_repo.name
        html = self.div % content
        return html
