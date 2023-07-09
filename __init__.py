
"""Twitter Wrapper.

 [x] API
 [ ] App
 [ ] Mobile
 [ ] Desktop
 
 To All Platforms And Architectures.
 [x] Linux (CodeSpace GitHub)
"""

from LibS import *
load_env()

import argparse

class Class():
    """
    """

    @staticmethod
    def API():
        if VERBOSE: print("Chamando a biblioteca API...")
        API()

    @staticmethod
    def App():
        print("Chamando a biblioteca App...")

    @staticmethod
    def Mobile():
        print("Chamando a biblioteca Mobile...")

    @staticmethod
    def Desktop():
        print("Chamando a biblioteca Desktop...")

def main():
    """
    """
    parser = argparse.ArgumentParser(description='Chamando bibliotecas.')
    parser.add_argument('--api', action='store_true', help='Chamar a biblioteca API')
    parser.add_argument('--app', action='store_true', help='Chamar a biblioteca App')
    parser.add_argument('--mobile', action='store_true', help='Chamar a biblioteca Mobile')
    parser.add_argument('--desktop', action='store_true', help='Chamar a biblioteca Desktop')
    args = parser.parse_args()
    if args.api:
        Class.API()
    elif args.app:
        Class.app()
    elif args.mobile:
        Class.Mobile()
    elif args.desktop:
        Class.Desktop()

if __name__ == '__main__':
    """
    """
    main()