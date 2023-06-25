
"""
"""

from pymongo import MongoClient

class MongoDB():

    def __init__(self, *args, **kwargs):
        client = MongoClient(kwargs['dataBase'])
    
    def connect(self):
        print('mongodb')

def main():
    pass

if __name__ == '__main__':
    pass