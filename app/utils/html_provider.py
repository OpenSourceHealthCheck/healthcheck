import yapsy.IPlugin

class html_provider_base(yapsy.IPlugin.IPlugin):
    '''
    This is a base class for simple html content provider plugins
    '''

    # where in the results page the element should come (higher priority means
    # closer to the top).  This is because yapsy does not return plugins in
    # a fixed order.
    priority = 0
    
    def __init__(self):
        """
        Set the basic variables.
        """
        self.div = '''<div id="%s">%%s</div>''' % (self.__class__.__name__)
        self.passes = False

    def get_html(self, github_repo):
        '''
        github_repo is an repository object from github3
        This needs to return a html string which is enclosed in div tags specifying the plugin name
        i.e.
        self.div % content
        '''
        raise NotImplementedError("Your plugin needs to overload this method")
    
    def get_passes(self):
        '''
        will be called after get_html to see if this repo passes the test for this
        you will need to set the self.passes field in get_html
        returns a boolean
        '''
        return self.passes

    def __lt__(self, other):

        return self.priority < other.priority
