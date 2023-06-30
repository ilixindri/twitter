
"""
"""

import os

from . import SQLite
SQLite = SQLite.Class

from . import MongoDB
MongoDB = MongoDB.Class

class Class():
    """
    collections: BinS, DataS, LibS.
    """

    @staticmethod
    def function(*args, **kwargs):
        """
        """
        if DATABASE.startswith('mongodb'):
            return MongoDB()
        elif DATABASE == 'sqlite':
            return SQLite()

def main():
    Class()

if __name__ == '__main__':
    main()