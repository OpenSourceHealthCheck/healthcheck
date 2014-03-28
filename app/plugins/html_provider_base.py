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
        self.div = '''<div id="%s">%%s</div>''' % (self.__class__.__name__)

    def get_html(self, github_repo):
        '''
        github_repo is an repository object from github3
        This needs to return a html string which is enclosed in div tags specifying the plugin name
        i.e.
        self.div % content
        '''
        raise NotImplementedError("Your plugin needs to overload this method")
