import app.utils.html_provider as html_provider

class citation(html_provider.html_provider_base):

    priority =  12
    
    def find_citation(self, repo):
        # Get all files in the root directory of the repo
        root_files = repo.contents('/')

        possible_filenames = ['CITATION']

        try:
            root_files_iter = root_files.iteritems()
        except AttributeError:
            # python 3!
            root_files_iter = root_files.items()

        for name, contents in root_files_iter:
            for poss_name in possible_filenames:
                if poss_name in name.upper():
                    return name

    def get_html(self, repo):
        '''
        Checks if a CITATION file exists
        '''
        citation = self.find_citation(repo)

        if citation is None:
            # No readme!
            content = """The repository doesn't have a CITATION file - adding one could encourage people
            to reference your code. See <a href="http://www.software.ac.uk/blog/2013-09-02-encouraging-citation-software-introducing-citation-files">here</a> for more information."""
        else:
            # Yes readme!
            content = "Great - there's a CITATION file here"
            self.passes = True

        html = self.div % content
        return html

