
"""
"""

class Class():

    @staticmethod
    def function(*arg, **wargs):
        for key, value in wargs.items():
            globals()[key] = value