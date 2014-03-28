class html_provider_base():
    '''
    This is a base class for simple html content provider plugins
    '''
    
    def get_html(self, github_repo):
        '''
        This needs to return a html string which is enclosed in div tags specifying the plugin name
        i.e.
        <div id="MyPlygin">
        all content
        </div>
        '''
        raise NotImplementedError("Your plugin needs to overload this method")