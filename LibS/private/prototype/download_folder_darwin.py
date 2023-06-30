
"""
"""

class Class():
    """
    """

    def function(*args, **wargs):
        """
        """
        try:
            from Foundation import NSFileManager, NSSearchPathForDirectoriesInDomains, NSSearchPathDirectory
            download_folder = NSSearchPathForDirectoriesInDomains(NSSearchPathDirectory.NSDownloadsDirectory, NSSearchPathDirectory.NSUserDomainMask, True)[0]
            return download_folder
        except ImportError:
            return None

def main(*args, **wargs):
    """
    """
    Class()

if __name__ == '__main__':
    main()