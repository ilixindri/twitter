
"""Generate DataS And Interface To Write Libs.
"""

from LibS import *
load_env()

import LibS.DataS
DataS = LibS.DataS.Class.function

class Class():
    """
    """

    def __init__(self, *args, **wargs):
        """
        """
        dataS = DataS()
        collection = 'BinS'
        document = {'title': '', 'content': ''}
        dataS.insert(collection=collection, document=document)

def main(*args, **wargs):
    """
    """
    Class()

if __name__ == '__main__':
    """
    """
    main()