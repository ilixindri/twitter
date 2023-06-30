
"""
"""

from dotenv import load_dotenv
load_dotenv()

import os

class Class():
    """
    """

    def function(*args, **wargs):
        """
        """
        for key, value in os.environ.items():
            try:
                __builtins__[key] = eval(value)
            except SyntaxError as e:
                __builtins__[key] = value
            except NameError as e:
                __builtins__[key] = value

def main():
    """
    """
    Class()

if __name__ == '__main__':
    """
    """
    main()