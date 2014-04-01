import app.utils.html_provider as html_provider

class is_my_code_ready(html_provider.html_provider_base):

    priority =  25
    
    def get_html(self, github_repo):
        '''
        Simple Implementation for testing
        '''
        content = "%s is ready to share :)  <a href='http://shouldisharemyco.de#%s'>Check this on ShouldIShareMyCo.de</a>" % (github_repo.name,github_repo.git_url)
        html = self.div % content
        self.passes = True

        return html
