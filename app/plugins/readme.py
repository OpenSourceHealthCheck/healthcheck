import github3
from html_provider_base import html_provider_base

class readme(html_provider_base):
    
    def get_html(self, repo):
        '''
        Checks if a README file exists
        '''

        button = """<form method="POST" action="/create_issue">
        <input type="hidden" name="repo" value="%s">
        <input type="hidden" name="user" value="%s">
        <input type="submit" value="Add an issue"></form>""" % (repo.name, repo.owner)

        readme = repo.readme()

        if readme is None:
            # No readme!
            content = """The repository doesn't have a README file.
This is essential to make it easy for other people to use your code. We can automatically add an issue
to the project to ask the developers to create one.\n""" + button
        else:
            # Yes readme!
            content = "Great - there's a README file here"
            readme_contents = readme.decoded
            if "contrib" in readme_contents:
                content += " - and it even looks like there's some contributing information!"

        html = self.div % content
        return html
