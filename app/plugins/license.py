import github3
from html_provider_base import html_provider_base

class license(html_provider_base):
    
    def find_licenses(self, repo):
        # Get all files in the root directory of the repo
        root_files = repo.contents('/')

        possible_filenames = ['COPYING', 'LICENSE']

        for name, contents in root_files.iteritems():
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

        if license_filename is None:
            # No license found!
            content = "No license found!"
        else:
            # License is available, so get the content of it
            license = self.get_file(repo, license_filename).upper()

            if "LESSER" in license or self.file_exists(repo, 'COPYING.LESSER'):
                license_type = "LGPL"
            elif "GNU GENERAL PUBLIC LICENSE" in license:
                license_type = "GPL"
            elif " MIT " in license:
                license_type = "MIT"
            else:
                license_type = None

            if license_type is not None:
                content = "Well done! This code is licensed under the %s license." % (license_type)
            else:
                content = "Well done! This code is licensed, but we can't work out what license it is using. Is it a standard open-source licence?"


        html = self.div % content
        return html
