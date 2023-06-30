
"""
"""

import sys
import os

class Class():
    """
    """

    @staticmethod
    def _is_linux(*args, **wargs):
        """
        """
        return sys.platform == "linux" or sys.platform == "linux2"

def main():
    Class()

if __name__ == '__main__':
    main()