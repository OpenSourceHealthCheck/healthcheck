from yapsy import IPlugin

class html_provider_base(IPlugin):
    '''
    This is a base class for simple html content provider plugins
    '''
    
    def __init__(self):
        """
        Set the basic variables.
        """
        self.is_activated = False
    
    def get_html(self, github_repo):
        '''
        github_repo is an repository object from github3
        This needs to return a html string which is enclosed in div tags specifying the plugin name
        i.e.
        <div id="MyPlygin">
        all content
        </div>
        '''
        raise NotImplementedError("Your plugin needs to overload this method")