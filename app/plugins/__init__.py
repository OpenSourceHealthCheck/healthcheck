from is_my_code_ready_plugin import is_my_code_ready
from stats_plugin import stats

def load():
    return [is_my_code_ready(), stats()]