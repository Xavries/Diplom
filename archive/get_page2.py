#import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import random

options = Options()
#options.page_load_strategy = 'eager'

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

wait_time0 = 5
wait_time1 = 8
driver = webdriver.Firefox(firefox_options=options, firefox_profile=profile)#, desired_capabilities=desired)
driver.maximize_window()
#driver = webdriver.Firefox()
######################### Chromium Plating ############################
ttspage = "div>"
while len(ttspage.split("div")) < 100:
	driver.implicitly_wait(random.uniform(wait_time0, wait_time1))
	driver.get("https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=18124&ItemNamePattern=Chromium+Plating&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=130000")
	driver.implicitly_wait(random.uniform(wait_time0, wait_time1))
	wait = WebDriverWait(driver, 5, poll_frequency=1)
	element = driver.find_element_by_id("search-result-view")
	#element1 = element.find_element_by_tag_name("div")

	ttspage = element.get_attribute("outerHTML")
	#print(ttspage)#, '\n', element1, '\n')
	print(type(ttspage.split("div")),  '\n', len(ttspage.split("div")))
#if len(ttspage.split("div"))<120:
print("Chromium Plating")
f = open("ttspage1.html", "w")
f.write(ttspage)
f.close()

ttspage = "div>"
while len(ttspage.split("div")) < 100:
	userAgent = ua.random
	options.add_argument(f'user-agent={userAgent}')
	print(userAgent)
	#driver.get("https://support.mozilla.org/en-US/kb/diagnose-firefox-issues-using-troubleshoot-mode")
	######################### Zircon Plating ############################
	driver.implicitly_wait(random.uniform(wait_time0, wait_time1))
	driver.get("https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=17799&ItemNamePattern=Zircon+Plating&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=35000")
	driver.implicitly_wait(random.uniform(wait_time0, wait_time1))
	wait = WebDriverWait(driver, 5, poll_frequency=1)
	element = driver.find_element_by_id("search-result-view")

	ttspage = element.get_attribute("outerHTML")
	#print(ttspage)
	print(type(ttspage.split("div")),  '\n', len(ttspage.split("div")))
	#
print("Zircon Plating")
f = open("ttspage1.html", "a")
f.write(ttspage)

ttspage = "div>"
while len(ttspage.split("div")) < 100:
	userAgent = ua.random
	options.add_argument(f'user-agent={userAgent}')
	print(userAgent)
	#driver.get("https://support.mozilla.org/en-US/questions/new/mobile")
	######################### Potent Nirncrux ############################
	driver.implicitly_wait(random.uniform(wait_time0, wait_time1))
	driver.get("https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=3790&ItemNamePattern=Potent+Nirncrux&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=21000")
	driver.implicitly_wait(random.uniform(wait_time0, wait_time1))
	wait = WebDriverWait(driver, 5, poll_frequency=1)
	element = driver.find_element_by_id("search-result-view")

	ttspage = element.get_attribute("outerHTML")
	print(type(ttspage.split("div")),  '\n', len(ttspage.split("div")))
	#
print("Potent Nirncrux")

f.write(ttspage)

ttspage = "div>"
while len(ttspage.split("div")) < 100:
	userAgent = ua.random
	options.add_argument(f'user-agent={userAgent}')
	print(userAgent)
	#driver.get("https://support.mozilla.org/en-US/questions/new/firefox-private-network")
	######################### Perfect Roe ############################
	driver.implicitly_wait(random.uniform(wait_time0, wait_time1))
	driver.get("https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=6132&ItemNamePattern=Perfect+Roe&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=21000")
	driver.implicitly_wait(random.uniform(wait_time0, wait_time1))
	wait = WebDriverWait(driver, 5, poll_frequency=1)
	element = driver.find_element_by_id("search-result-view")

	ttspage = element.get_attribute("outerHTML")
	print(type(ttspage.split("div")),  '\n', len(ttspage.split("div")))
	#
print("Perfect Roe")

f.write(ttspage)

ttspage = "div>"
while len(ttspage.split("div")) < 100:
	userAgent = ua.random
	options.add_argument(f'user-agent={userAgent}')
	print(userAgent)
	#driver.get("https://www.mozilla.org/en-US/firefox/channel/android/?utm_source=support.mozilla.org&utm_campaign=footer&utm_medium=referral#nightly")
	######################### Hakeijo ############################
	driver.implicitly_wait(random.uniform(wait_time0, wait_time1))
	driver.get("https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=4794&ItemNamePattern=Hakeijo&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=32500")
	driver.implicitly_wait(random.uniform(wait_time0, wait_time1))
	wait = WebDriverWait(driver, 5, poll_frequency=1)
	element = driver.find_element_by_id("search-result-view")

	ttspage = element.get_attribute("outerHTML")
	print(type(ttspage.split("div")),  '\n', len(ttspage.split("div")))
	#
print("Hakeijo")

f.write(ttspage)

ttspage = "div>"
while len(ttspage.split("div")) < 100:
	userAgent = ua.random
	options.add_argument(f'user-agent={userAgent}')
	print(userAgent)
	#driver.get("https://www.mozilla.org/en-US/about/manifesto/")
	######################### Dreugh Wax ############################
	driver.implicitly_wait(random.uniform(wait_time0, wait_time1))
	driver.get("https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=211&ItemNamePattern=Dreugh+Wax&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=12000")
	driver.implicitly_wait(random.uniform(wait_time0, wait_time1))
	wait = WebDriverWait(driver, 5, poll_frequency=1)
	element = driver.find_element_by_id("search-result-view")

	ttspage = element.get_attribute("outerHTML")
	print(type(ttspage.split("div")),  '\n', len(ttspage.split("div")))
	#
print("Dreugh Wax")

f.write(ttspage)

ttspage = "div>"
while len(ttspage.split("div")) < 100:
	userAgent = ua.random
	options.add_argument(f'user-agent={userAgent}')
	print(userAgent)
	#driver.get("https://monitor.firefox.com/")
	######################### Tempering Alloy ############################
	driver.implicitly_wait(random.uniform(wait_time0, wait_time1))
	driver.get("https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=5687&ItemNamePattern=Tempering+Alloy&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=6000")
	driver.implicitly_wait(random.uniform(wait_time0, wait_time1))
	wait = WebDriverWait(driver, 5, poll_frequency=1)
	element = driver.find_element_by_id("search-result-view")

	ttspage = element.get_attribute("outerHTML")
	print(type(ttspage.split("div")),  '\n', len(ttspage.split("div")))
	#
print("Tempering Alloy")

f.write(ttspage)

f.close()

print("Done.")

driver.quit()
