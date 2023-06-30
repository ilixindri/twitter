
"""
"""

class Class():
    """
    """

    def function(*args, **wargs):
        """
        """
        try:
            from xdg import user_dirs
            return user_dirs.download
        except ImportError:
            return None


def main(*args, **wargs):
    """
    """
    Class()

if __name__ == '__main__':
    main()