
"""
"""

class Class():

    def function(*args, **wargs):
        for _ in args:
            pip.main(['install', _])

def main():
    Class()

if __name__ == '__main__':
    main()