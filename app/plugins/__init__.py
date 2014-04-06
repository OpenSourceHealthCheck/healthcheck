import os
from app.plugins.is_my_code_ready_plugin import is_my_code_ready
from app.plugins.weekly_commits_plugin import weekly_commits
from app.plugins.license import license
from app.plugins.readme import readme
from app.plugins.busfactor import busfactor

def load():
    return [is_my_code_ready(), 
            license(), 
            readme(),
            busfactor(),
            weekly_commits()]
