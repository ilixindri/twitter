
"""
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Lib():

    def __init__(self, *args, **kwargs):
        global driver
        global delay
        self.wait = WebDriverWait(driver, delay)

    def g(self, *args, **kwargs):
        if args[0].startswith('/') or args[0].startswith('.'):
            _0xfe = args[0]
            _0xff = args[1]
        else:
            _0xfe = args[1]
            _0xff = args[0]
        try:
            return self.wait.until(EC.visibility_of_all_elements_located((_0xff, _0xfe)))
        except:
            return self.g(*args)