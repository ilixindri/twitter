
"""
"""

headless = False
if headless:
    delay = 3
else:
    delay = 10

import pip
try: import selenium
except: pip.main(['install', 'selenium==4.10.0'])
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
from lib import Lib
from dotenv import load_dotenv

load_dotenv()
for key, value in os.environ.items():
    globals()[key] = value

class CV(Lib):
    def __init__(self):
        user = os.path.expanduser('~')
        edge_driver_path = os.path.join(user, r"OneDrive\Downloads\edgedriver_win64\msedgedriver.exe")
        edge_executable_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        options = Options()
        options.use_chromium = True
        if headless:
            options.add_argument("--headless")
        options.add_argument("--ignore-ssl-errors=yes")
        options.add_argument("--ignore-certificate-errors")
        options.binary_location = edge_executable_path
        service = Service(edge_driver_path)
        driver = webdriver.Edge(service=service, options=options)
        driver.get("https://twitter.com/i/flow/login")
        e = self.g(By.XPATH, '//input[@type="text"]')
        e.send_keys(USER)
        e = self.g(By.CSS_SELECTOR, '.css-18t94o4.css-1dbjc4n.r-sdzlij.r-1phboty.r-rs99b7.r-ywje51.r-usiww2.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr.r-13qz1uu')
        e.click()
        e = self.g(By.XPATH, '//input[@type="password"]')
        e.send_keys(PASS)
        e = self.g(By.XPATH, '//div[@data-testid="LoginForm_Login_Button"]')
        e.click()
        driver.get("https://twitter.com/search?q=comando%20vermelho&src=typed_query&f=user")
        _0x02 = set()
        def _0x03(_0x02=_0x02, _0x01=_0x01):
            for e in _0x01:
                _0x02.add(e.get_attribute('href'))
            return _0x02
        _0x04 = 0
        _0x05 = None
        while _0x04 != _0x05:
            _0x01 = driver.find_elements('xpath', '//a[@role="link"]')
            _0x02 = _0x03()
            _0x05 = len(_0x02)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print(_0x02)

def main():
    CV()

if __name__ == '__name__':
    main()