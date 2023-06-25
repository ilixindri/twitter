
"""
"""

import os
from SQLite import SQLite
from MongoDB import MongoDB

class DataBase(SQLite, MongoDB):

    def __init__(self, *args, **kwargs):
        dataBase = os.getenv('DATABASE')
        if dataBase.startswith('mongodb'):
            super(MongoDB)
        elif dataBase == 'sqlite':
            super(SQLite)
        else:
            raise NotImplementedError

def main():
    DataBase()

if __name__ == '__main__':
    main()