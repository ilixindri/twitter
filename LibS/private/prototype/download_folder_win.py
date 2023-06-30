
"""
"""

import ctypes
from ctypes import wintypes

def function():
    FOLDERID_Downloads = '{374DE290-123F-4565-9164-39C4925E467B}'

    shell32 = ctypes.windll.shell32

    SHGetKnownFolderPath = shell32.SHGetKnownFolderPath
    SHGetKnownFolderPath.argtypes = [
        ctypes.POINTER(ctypes.wintypes.GUID),
        wintypes.DWORD,
        wintypes.HANDLE,
        ctypes.POINTER(ctypes.c_wchar_p)
    ]
    SHGetKnownFolderPath.restype = wintypes.HRESULT

    pszPath = ctypes.c_wchar_p()
    result = SHGetKnownFolderPath(ctypes.byref(ctypes.wintypes.GUID(FOLDERID_Downloads)), 0, 0, ctypes.byref(pszPath))

    if result == 0:
        download_folder = pszPath.value
        ctypes.windll.ole32.CoTaskMemFree(pszPath)
        return download_folder
    else:
        return None