import github3
from app.plugins.html_provider_base import html_provider_base

class license(html_provider_base):

    
    def find_licenses(self, repo):
        # Get all files in the root directory of the repo
        root_files = repo.contents('/')

        possible_filenames = ['COPYING', 'LICENSE']

        try:
            root_files_iter = root_files.iteritems()
        except AttributeError:
            # python 3!
            root_files_iter = root_files.items()

        for name, contents in root_files_iter:
            for poss_name in possible_filenames:
                if poss_name in name.upper():
                    return name

    def get_file(self, repo, path):
        return repo.contents(path).decoded

    def file_exists(self, repo, path):
        return repo.contents(path) is not None

    def get_html(self, repo):
        '''
        Tries to find a license, and if it can then guesses what license it is
        '''
        license_filename = self.find_licenses(repo)

        body = "Please add a LICENSE file to your repository.\nNot having a license creates all sorts of problems, so we strongly suggest you add one.\n\n(This issue was created by the Open Source Health Check tool at www.healthcheck.io)"
        title = "Add a LICENSE"

        button = """<form method="POST" action="/create_issue">
        <input type="hidden" name="repo" value="%s">
        <input type="hidden" name="user" value="%s">
        <input type="hidden" name="body" value="%s">
        <input type="hidden" name="title" value="%s">
        <input type="submit" value="Add an issue"></form>""" % (repo.name, repo.owner, body, title)


        if license_filename is None:
            # No license found!
            content = "There isn't a license for this code which causes <b>major</b> problems. " + button
        else:
            # License is available, so get the content of it
            license = self.get_file(repo, license_filename).upper().decode()

            if "LESSER" in license or self.file_exists(repo, 'COPYING.LESSER'):
                license_type = "LGPL"
            elif "GNU GENERAL PUBLIC LICENSE" in license:
                license_type = "GPL"
            elif " MIT " in license:
                license_type = "MIT"
            elif "(INCLUDING NEGLIGENCE OR OTHERWISE)" in license:
                license_type = "BSD"
            else:
                license_type = None

            if license_type is not None:
                self.passes = True
                content = "Well done! This code is licensed under the %s license." % (license_type)
            else:
                content = "Well done! This code is licensed, but we can't work out what license it is using. Is it a standard open-source licence?"


        html = self.div % content
        return html
