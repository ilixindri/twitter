
"""
"""

from dotenv import load_dotenv
from DataBase import DataBase

def main():
    load_dotenv()
    database = DataBase()
    database.connect()

if __name__ == '__main__':
    main()