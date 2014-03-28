import github3

class is_my_code_ready(html_provider_base):
    
    def get_html(self, github_repo):
        '''
        Simple Implementation for testing
        '''
        html ="<div id='is_my_code_ready'>%s is ready to share :)</div>" % (github_repo.name)
        return html
