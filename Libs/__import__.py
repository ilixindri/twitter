
"""
"""

from itertools import permutations
from _get_version import function as _get_version
from __imports__ import Class as __imports__
from _update_globals import Class as _update_globals
from _def_pkg import Class as _def_pkg

class Class():

    @staticmethod
    def function(*args, **wargs):
        """
        version=version, module=module, pkg=pkg
        """
        _update_globals.function(*args, **wargs)
        _def_pkg.function(**wargs)
        try:
            line = f'import {module}'
            exec(line)
        except ModuleNotFoundError:
            exec('import pip')
            pip.main(['install', pkg])
            __import__(*args, **wargs)