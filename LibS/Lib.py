
"""
"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Class():

    def g(self, *args, **kwargs):
        if args[0].startswith('/') or args[0].startswith('.'):
            _0xfe = args[0]
            _0xff = args[1]
        else:
            _0xfe = args[1]
            _0xff = args[0]
        try:
        #if True:
            _0xfd = WebDriverWait(self.driver, self.delay).until(EC.visibility_of_all_elements_located((_0xff, _0xfe)))
            #time.sleep(30)
            print(',')
            return _0xfd
        except:
            print('.', end='')
            return self.g(*args)