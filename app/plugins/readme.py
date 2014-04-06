import app.utils.html_provider as html_provider

class readme(html_provider.html_provider_base):

    priority =  15
    
    def get_html(self, repo):
        '''
        Checks if a README file exists
        '''

        body = "Please add a README file to your repository.\nThis really helps to improve the sustainability of your software, and helps others pick up your code and get running with it easily.\n\n(This issue was created by the Open Source Health Check tool at www.healthcheck.io)"
        title = "Add a README"

        button = """<form method="POST" action="/create_issue">
        <input type="hidden" name="repo" value="%s">
        <input type="hidden" name="user" value="%s">
        <input type="hidden" name="body" value="%s">
        <input type="hidden" name="title" value="%s">
        <input type="submit" value="Add an issue"></form>""" % (repo.name, repo.owner, body, title)


        readme = repo.readme()

        if readme is None:
            # No readme!
            content = """The repository doesn't have a README file.
This is essential to make it easy for other people to use your code. """ + button
        else:
            # Yes readme!
            content = "Great - there's a README file here"
            self.passes = True
            readme_contents = readme.decoded
            if "contrib" in readme_contents.decode():
                content += " - and it even looks like there's some contributing information!"

        html = self.div % content
        return html

