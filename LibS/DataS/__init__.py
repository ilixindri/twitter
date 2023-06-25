
"""
"""

import os
from . import SQLite
from . import MongoDB

class Class(SQLite.Class, MongoDB.Class):

    def __init__(self, *args, **kwargs):
        if DATABASE.startswith('mongodb'):
            super(Class, self).__init__()
        elif DATABASE == 'sqlite':
            super(SQLite.Class, self).__init__()

def main():
    Class()

if __name__ == '__main__':
    main()