import pip
import time
try: import selenium
except: pip.main(['install', 'selenium==4.10.0'])
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
edge_driver_path = r"C:\Users\Administrator\OneDrive\Downloads\edgedriver_win64\msedgedriver.exe"
edge_executable_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
options = Options()
options.use_chromium = True
options.add_argument("--headless")
options.binary_location = edge_executable_path
service = Service(edge_driver_path)
username = input("Digite o nome de usuário do Twitter: ")
password = input("Digite a senha do Twitter: ")
#username = ""
#password = ""
driver = webdriver.Edge(service=service, options=options)
driver.get("https://twitter.com/i/flow/login")
time.sleep(3)
username_input = driver.find_element('xpath', '//input[@type="text"]')
username_input.send_keys(username)
login_button = driver.find_element("css selector", '.css-18t94o4.css-1dbjc4n.r-sdzlij.r-1phboty.r-rs99b7.r-ywje51.r-usiww2.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr.r-13qz1uu')
login_button.click()
time.sleep(3)
password_input = driver.find_element('xpath', '//input[@type="password"]')
password_input.send_keys(password)
login_button = driver.find_element("xpath", '//div[@data-testid="LoginForm_Login_Button"]')
login_button.click()
time.sleep(3)
cookies = driver.get_cookies()
print("Cookies obtidos:")
for cookie in cookies:
    print(cookie)
driver.quit()