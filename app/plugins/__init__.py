import os
from is_my_code_ready_plugin import is_my_code_ready
from weekly_commits_plugin import weekly_commits
from license import license
from readme import readme
from busfactor import busfactor

def load():
    return [is_my_code_ready(), 
            license(), 
            readme(),
            weekly_commits(),
            busfactor()]
