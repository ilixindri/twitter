import urllib.parse
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

search = "comando vermelho"
encoded_search = urllib.parse.quote(search)
url = f"https://twitter.com/search?q={encoded_search}&src=typed_query&f=user"

driver = webdriver.Edge(EdgeChromiumDriverManager().install())

driver.get(url)
elements = driver.find_elements_by_css_selector('.css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0')
for element in elements:
    print(element.text)

driver.quit()