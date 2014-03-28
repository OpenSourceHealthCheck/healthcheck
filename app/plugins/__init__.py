import os
from is_my_code_ready_plugin import is_my_code_ready
from license import license

def load():
    return [is_my_code_ready(), license()]
