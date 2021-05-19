#import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

options = Options()
options.page_load_strategy = 'eager'
ua = UserAgent()
userAgent = ua.random
print(userAgent)
options.add_argument(f'user-agent={userAgent}')

profile = webdriver.FirefoxProfile()#"/home/linp/.mozilla/firefox/xjlukkfp.default-release")

PROXY_HOST = "12.12.12.123"
PROXY_PORT = "1234"
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.http", PROXY_HOST)
profile.set_preference("network.proxy.http_port", int(PROXY_PORT))

profile.set_preference("dom.webdriver.enabled", False)
profile.set_preference('useAutomationExtension', False)
profile.update_preferences()
#desired = DesiredCapabilities.FIREFOX

driver = webdriver.Firefox(firefox_options=options, firefox_profile=profile)
#, desired_capabilities=desired)
#driver = webdriver.Firefox()
driver.implicitly_wait(6.31)
driver.get("https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=18124&ItemNamePattern=Chromium+Plating&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=125000")
driver.implicitly_wait(5.11)
wait = WebDriverWait(driver, 5, poll_frequency=1)
element = driver.find_element_by_id("search-result-view")
element1 = element.find_element_by_tag_name("div")
#for i in element:
#	print(i.get_attribute("innerHTML"), '----', i.get_attribute("outerHTML"), '\n')

'''elementSource1 = driver.find_elements_by_tag_name("span")
for i in elementSource1:
	print(i.get_attribute("innerHTML"), '----', i.get_attribute("outerHTML"), '\n')
'''
print(element.get_attribute("outerHTML"))#, '\n', element1, '\n')

driver.quit()
