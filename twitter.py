import pip
try: import requests
except: pip.main(['install', 'requests']); import requests








import pip
import time
headless = True
if headless:
    delay_basic = 3
else:
    delay_basic = 10
try: import selenium
except: pip.main(['install', 'selenium==4.10.0'])
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
try: import browsermobproxy
except: pip.main(['install', 'browsermob-proxy'])
from browsermobproxy import Server
path_to_browsermob_proxy = r"C:\Users\Administrator\OneDrive\Downloads\browsermob-proxy-2.1.4-bin\browsermob-proxy-2.1.4\bin\browsermob-proxy.bat"
server = Server(path_to_browsermob_proxy)
server.start()
proxy = server.create_proxy()
edge_driver_path = r"C:\Users\Administrator\OneDrive\Downloads\edgedriver_win64\msedgedriver.exe"
edge_executable_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
options = Options()
options.use_chromium = True
options.add_argument("--headless")q
options.add_argument(f'--proxy-server={proxy.proxy}')
options.add_argument("--ignore-ssl-errors=yes")
options.add_argument("--ignore-certificate-errors")
options.binary_location = edge_executable_path
service = Service(edge_driver_path)
#username = input("Digite o nome de usuário do Twitter: ")
#password = input("Digite a senha do Twitter: ")
username = "alexandrogonsan"
password = ""
driver = webdriver.Edge(service=service, options=options)
proxy.new_har("intercepted_requests", options={'captureHeaders': True, 'captureContent': False})
driver.get("https://twitter.com/i/flow/login")
time.sleep(delay_basic)
username_input = driver.find_element('xpath', '//input[@type="text"]')
username_input.send_keys(username)
login_button = driver.find_element("css selector", '.css-18t94o4.css-1dbjc4n.r-sdzlij.r-1phboty.r-rs99b7.r-ywje51.r-usiww2.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr.r-13qz1uu')
login_button.click()
time.sleep(delay_basic)
password_input = driver.find_element('xpath', '//input[@type="password"]')
password_input.send_keys(password)
login_button = driver.find_element("xpath", '//div[@data-testid="LoginForm_Login_Button"]')
login_button.click()
time.sleep(delay_basic*3)
cookies = driver.get_cookies()
har = proxy.har
csrf_tokens = []
for entry in har['log']['entries']:
    request = entry['request']
    headers = request['headers']
    for header in headers:
        if header['name'].lower() == 'x-csrf-token':
            csrf_tokens += [header['value']]
csrf_token = csrf_tokens[-1]
#driver.quit()
#server.stop()









session = requests.Session()
for cookie in cookies:
    session.cookies.set(cookie['name'], cookie['value'])

















url = 'https://twitter.com/i/api/graphql/GUFG748vuvmewdXbB5uPKg/CreateTweet'
headers = {
    'Host': 'twitter.com',
    'Connection': 'keep-alive',
    'Content-Length': '1036',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
    'x-twitter-client-language': 'pt',
    'x-csrf-token': csrf_token,
    'sec-ch-ua-mobile': '?0',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.0.0',
    'content-type': 'application/json',
    'x-twitter-auth-type': 'OAuth2Session',
    'x-client-uuid': '0e0ef923-470b-4485-84b9-82969b0a3316',
    'x-twitter-active-user': 'yes',
    'sec-ch-ua-platform': '"Windows"',
    'Accept': '*/*',
    'Origin': 'https://twitter.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://twitter.com/home',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
#    'Cookie': '_ga=; _gid=4; ...'
}
body = {
    "variables": {
        "tweet_text": "Create by @python script with cookies of selenium and csrf-token by browsermob-proxy",
        "dark_request": False,
        "media": {
            "media_entities": [],
            "possibly_sensitive": False
        },
        "semantic_annotation_ids": []
    },
    "features": {
        "tweetypie_unmention_optimization_enabled": True,
        "responsive_web_edit_tweet_api_enabled": True,
        "graphql_is_translatable_rweb_tweet_is_translatable_enabled": True,
        "view_counts_everywhere_api_enabled": True,
        "longform_notetweets_consumption_enabled": True,
        "tweet_awards_web_tipping_enabled": False,
        "longform_notetweets_rich_text_read_enabled": True,
        "longform_notetweets_inline_media_enabled": True,
        "responsive_web_graphql_exclude_directive_enabled": True,
        "verified_phone_label_enabled": False,
        "freedom_of_speech_not_reach_fetch_enabled": True,
        "standardized_nudges_misinfo": True,
        "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": False,
        "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False,
        "responsive_web_graphql_timeline_navigation_enabled": True,
        "responsive_web_enhance_cards_enabled": False
    },
    "queryId": "GUFG748vuvmewdXbB5uPKg"
}
#response = requests.post(url, headers=headers, json=body)
response = session.post(url, headers=headers, json=body)
print(response.status_code)
#print(response.json())

















driver.quit()
server.stop()