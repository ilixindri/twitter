
"""
"""

from pymongo import MongoClient

class Class():
    """
    """

    def __init__(self, *args, **kwargs):
        """
        """
        if VERBOSE: print('setting client')
        self.client = MongoClient(DATABASE)
        if VERBOSE: print('setting db')
        self.db = self.client['TwitterS']

    def insert(self, *args, **wargs):
        """
        collection=collection, document=document
        """
        if VERBOSE: print('update wargs')
        self.__dict__.update(wargs)
        if VERBOSE: print('setting collection')
        collection = self.db[self.collection]
        if VERBOSE: print('making insert')
        result = collection.insert_one(self.document)
        if VERBOSE: print('returning result')
        return result.inserted_id

def main():
    """
    """
    Class()

if __name__ == '__main__':
    """
    """
    main()