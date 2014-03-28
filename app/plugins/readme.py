import github3
from html_provider_base import html_provider_base

class readme(html_provider_base):
    
    def get_html(self, repo):
        '''
        Checks if a README file exists
        '''

        readme = repo.readme()

        if readme is None:
            # No readme!
            content = "The repository doesn't have a README file. This is essential to make it easy for other people to use your code."
        else:
            # Yes readme!
            content = "Great - there's a README file here"
            readme_contents = readme.decoded
            if "contrib" in readme_contents:
                content += " - and it even looks like there's some contributing information!"

        html = self.div % content
        return html
