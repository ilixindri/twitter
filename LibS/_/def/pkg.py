
"""
"""

import traceback

class Class():

    @staticmethod
    def function(*args, **wargs):
        try:
            globals()['pkg'] = globals()['pkg']
            globals()['pkg'] = globals()['pkg'] + '==' + globals()['version']
            globals()['pkg'] = globals()['module'] + '==' + globals()['version']
        except KeyError as e:
            if str(e).split('\n')[-1].split(' ')[-1].replace("'", "") == 'pkg':
                globals()['pkg'] = globals()['module']
                function(*args, **wargs)