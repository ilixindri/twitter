
"""
"""

from OneDrive import Class as OneDrive
from MegaNZ import Class as MegaNZ
from GoogleDrive import Class as GoogleDrive

lower = str.lower

class Class(OneDrive, MegaNZ, GoogleDrive):
    """
    """

    def __init__(self, *args, **kwargs):
        if lower(CLOUD) == lower('OneDrive'):
            super(OneDrive)
        elif lower(CLOUD) == lower('MegaNZ'):
            super(MegaNZ)
        elif lower(CLOUD) == lower('GoogleDrive'):
            super(GoogleDrive)
        else:
            raise NotImplementedError

    def function(*args, **wargs):
        """
        """
        pass

def main(*args, **wargs):
    """
    """
    Class()

if __name__ == '__main__':
    main()