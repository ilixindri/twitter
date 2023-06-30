
"""
"""

from Libs._download_folder._win import function as _download_folder_win
from Libs._download_folder._linux import function as _download_folder_linux
from Libs._download_folder._darwin import function as _download_folder_darwin
from Libs.is._win import function as _is_win
from Libs.is._linux import function as _is_linux
from Libs.is._darwin import function as _is_darwin

class Class():
    """
    """

    def function(*args, **wargs):
        """
        """
        if _is_win():
            return _download_folder_win()
        elif _is_linux():
            return _download_folder_linux()
        elif _is_darwin():
            return _download_folder_darwin()
        raise NotImplementedError

def main(*args, **wargs):
    """
    """
    Class()

if __name__ == '__main__':
    main()