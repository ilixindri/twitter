
"""
"""

from Libs.index import __import__, __imports__

__import__('selenium', '4.10.0')
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

__imports__(('screeninfo'), ('dotenv', 'python-dotenv'))
from screeninfo import get_monitors
from dotenv import load_dotenv

__imports__(('os'), ('time'))
import os
import time

__imports__(('pygetwindow'))
import pygetwindow as gw

load_dotenv()
for key, value in os.environ.items():
    globals()[key] = eval(value)
if not HEADLESS:
    DELAY *= 3

class CV(Lib):
    def __init__(self, *args, **kwargs):
        self.delay = args[0]
        self.verbose = args[1]
        user = os.path.expanduser('~')
        edge_driver_path = os.path.join(user, r"OneDrive\Downloads\edgedriver_win64\msedgedriver.exe")
        edge_executable_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        options = Options()
        options.use_chromium = True
        if HEADLESS:
            options.add_argument("--headless")
        options.add_argument("--ignore-ssl-errors=yes")
        options.add_argument("--ignore-certificate-errors")
        options.binary_location = edge_executable_path
        service = Service(edge_driver_path)
        self.driver = webdriver.Edge(service=service, options=options)
        self.driver.get("https://twitter.com/i/flow/login")
        es = self.g(By.XPATH, '//input[@type="text"]')
        es[0].send_keys(USER)
        time.sleep(self.delay)
        es = self.g(By.CSS_SELECTOR, '.css-18t94o4.css-1dbjc4n.r-sdzlij.r-1phboty.r-rs99b7.r-ywje51.r-usiww2.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr.r-13qz1uu')
        es[0].click()
        if verbose: print('user entered')
        es = self.g(By.XPATH, '//input[@type="password"]')
        es[0].send_keys(PASS)
        time.sleep(self.delay)
        es = self.g(By.XPATH, '//div[@data-testid="LoginForm_Login_Button"]')
        es[0].click()
        if verbose: print('pass entered')
        if verbose: print('login')
        self.g(By.CSS_SELECTOR, '//div[@data-offset-key="data-offset-key"]')
        self.driver.get("https://twitter.com/search?q=comando%20vermelho&src=typed_query&f=user")
        _0x02 = set()
        _0x04 = 0
        _0x05 = None
        while _0x04 != _0x05:
            _0x01 = self.g(By.XPATH, '//a[@role="link"]')
            def _0x03(_0x02=_0x02, _0x01=_0x01):
                for e in _0x01:
                    _0x02.add(e.get_attribute('href'))
                return _0x02
            _0x02 = _0x03()
            _0x05 = len(_0x02)
            e = self.driver.find_element(By.TAG_NAME, "body")
            e.send_keys(Keys.END)
            print('END pressed')
        print(_0x02)

def main():
    CV(delay, verbose)

if __name__ == '__main__':
    main()