'''
import urllib
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=18124&ItemNamePattern=Chromium+Plating&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=125000"

response = urlopen(url)
htmltext = BeautifulSoup(response)

with open("item_page_SOUP.txt", "w", encoding='utf-8') as file:
    file.write(str(htmltext))
    
print (htmltext)
for i in htmltext:
	print(type(i))
'''
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
driver.get("https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=18124&ItemNamePattern=Chromium+Plating&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=125000")

# waiting for the page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located(By.CSS_SELECTOR, ".odds-comparison"))

for comparison in driver.find_elements_by_css_selector(".odds-comparison"):
    description = comparison.find_element_by_css_selector(".description").text
    print(description)

driver.close()
'''

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
options = Options()
options.page_load_strategy = 'normal'

'''url = 'https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=18124&ItemNamePattern=Chromium+Plating&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=125000'
pythonResponse = requests.get(url)
fileToWrite = open("py_source.html", "w")
fileToWrite.write(pythonResponse.text)
fileToWrite.close()
fileToRead = open("py_source.html", "r")
print(fileToRead.read())
fileToRead.close()'''

driver = webdriver.Firefox()
driver.get("https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=Sell&ItemID=18124&ItemNamePattern=Chromium+Plating&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&LevelMin=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=125000")
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 5, poll_frequency=1)
element = driver.find_element_by_id("search-result-view")
element1 = element.find_element_by_tag_name("div")
#for i in element:
#	print(i.get_attribute("innerHTML"), '----', i.get_attribute("outerHTML"), '\n')

'''elementSource1 = driver.find_elements_by_tag_name("span")
for i in elementSource1:
	print(i.get_attribute("innerHTML"), '----', i.get_attribute("outerHTML"), '\n')
'''
print(element.get_attribute("outerHTML"), '\n', element1, '\n')

driver.quit()
