from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import random
import time

start_time = time.time()
#main()

options = Options()
#options.page_load_strategy = 'eager'

ua = UserAgent()
userAgent = ua.random
print(userAgent)
options.add_argument(f'user-agent={userAgent}')

profile = webdriver.FirefoxProfile()#"/home/linp/.mozilla/firefox/xjlukkfp.default-release")
print(webdriver.FirefoxProfile())
PROXY_HOST = "51.05.23.594"
PROXY_PORT = "6142"
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.http", PROXY_HOST)
profile.set_preference("network.proxy.http_port", int(PROXY_PORT))
profile.set_preference("dom.webdriver.enabled", False)
profile.set_preference('useAutomationExtension', False)
profile.update_preferences()
#desired = DesiredCapabilities.FIREFOX

get_pages = {"Chronium Plating":"https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=18124&ItemNamePattern=Chromium+Plating&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=130000", 
 "Zircon plating":"https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=17799&ItemNamePattern=Zircon+Plating&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=35000", 
 "Potent Nirncrux":"https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=3790&ItemNamePattern=Potent+Nirncrux&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=21000", 
 "Prefect Roe":"https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=6132&ItemNamePattern=Perfect+Roe&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=21000",
 "Hakejio":"https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=4794&ItemNamePattern=Hakeijo&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=32500", 
 "Dreugh Wax":"https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=211&ItemNamePattern=Dreugh+Wax&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=12000", 
 "Tempering Alloy":"https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=5687&ItemNamePattern=Tempering+Alloy&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=6000"}

driver = webdriver.Firefox(firefox_options=options, firefox_profile=profile)#, desired_capabilities=desired)
driver.maximize_window()
j = 0

for i in get_pages:
	ttspage = "div>"
	while len(ttspage.split("div")) < 100:
		#changing userAgent
		userAgent = ua.random
		options.add_argument(f'user-agent={userAgent}')
		print(userAgent)
		#gettig page
		time.sleep(random.uniform(10, 12))
		print("--- %s seconds ---" % (time.time() - start_time))
		driver.get(get_pages.get(i))
		time.sleep(random.uniform(1, 2))
		print("--- %s seconds ---" % (time.time() - start_time))
		#cut the page to get only half after <search-result-view>
		element = driver.find_element_by_id("search-result-view")
		#getting html from a page
		ttspage = element.get_attribute("outerHTML")
		#print(ttspage)
		print(len(ttspage.split("div")), j)
		j += 1
		
	print(f'------------------------------------{i}------------------------------------------')
	f = open("ttspage5.html", "a")
	f.write(ttspage)

print("Done.")

driver.quit()
