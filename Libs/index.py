
"""
"""

import pip

from Libs.LowLevelError import Class as LowLevelError

from itertools import permutations

def __import__(*args, **kwargs):
    """
    (version, module, pkg), ...
    """
    version, module = _get_version(args[0])
    try:
        for _ in module:
            line = f'import {_}'
            exec(line)
    except ModuleNotFoundError:
        if version is None:
            for _ in module:
                pip.main(['install', _])
                __import__(*args, **kwargs)
        elif version is not None:
            for _0x01, _0x02 in permutations(module):
                pkg = f'{_0x01}=={_0x02}'
                pip.main(['install', pkg])
                __import__(*args, **kwargs)

def __imports__(*args, **kwargs):
    for arg in args:
        __import__(arg)

def _get_version(*args, **kwargs):
    _0xff = list(range(len(args)))
    _0xfc = None
    for i in range(len(args)):
        if args[0][i][0].isdigit():
            _0xff.remove(i)
            _0xfc = args[0][i]
    _0xfe = set()
    for _0xfd in _0xff:
        _0xfe.add(args[0][_0xfd])
    return _0xfc, _0xfe